from django.db import transaction
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from chats.models import Chat, Message
from chats.serializers import ChatSerializer, MessageSerializer
from common.views import BaseViewSet
from openai_integration.openai_chat import Chat as OpenAIChat


class ChatViewSet(BaseViewSet, CreateModelMixin):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    @transaction.atomic
    async def create(self, request, *args, **kwargs):
        user = request.user
        chat = OpenAIChat()
        thread_id = chat.thread.id

        try:
            Chat.objects.create(
                user=user,
                thread_id=thread_id
            )
        except Exception as e:
            return self.handle_error(e, status.HTTP_500_INTERNAL_SERVER_ERROR, user.id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)


class MessageViewSet(BaseViewSet, CreateModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_fields = (
        'chat',
    )

    @transaction.atomic
    async def create(self, request, *args, **kwargs):
        try:
            chat = Chat.objects.get(id=request.data['chat'])
            content = request.data['content']
        except Exception as e:
            return self.handle_error(e, status.HTTP_400_BAD_REQUEST, request.user.id)

        try:
            chat = OpenAIChat(chat.thread_id)
            chat.create_user_message(content)
            run = chat.run_assistant()
            chat.wait_until_run_is_completed(run)
        except Exception as e:
            return self.handle_error(e, status.HTTP_500_INTERNAL_SERVER_ERROR, request.user.id)

        request_message = Message(
            chat=chat,
            role='user',
            content=content
        )

        response_message_content = run.content[0].text.value
        response_message = Message(
            chat=chat,
            role='assistant',
            content=response_message_content
        )

        serializer = self.get_serializer(data=[request_message, response_message], many=True)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)
