from django.db import transaction
from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from chats.models import Chat, Message
from chats.serializers import ChatSerializer, MessageSerializer, MessagePairSerializer
from common.views import BaseViewSet
from openai_integration.openai_chat import Chat as OpenAIChat


class ChatViewSet(BaseViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        user = request.user
        chat = OpenAIChat()
        thread_id = chat.thread.id

        try:
            chat_data = {
                'user': user.id,
                'thread_id': thread_id
            }
            serializer = self.get_serializer(data=chat_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except Exception as e:
            return self.handle_error(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR, user.id)

        return Response(status=status.HTTP_201_CREATED, data=serializer.data)


class MessageViewSet(BaseViewSet, CreateModelMixin):
    permission_classes = [IsAuthenticated]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_fields = (
        'chat',
    )

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        try:
            chat_id = request.data['chat']
            chat = Chat.objects.get(id=chat_id)
            content = request.data['content']
        except Exception as e:
            return self.handle_error(str(e), status.HTTP_400_BAD_REQUEST, request.user.id)

        try:
            openai_chat = OpenAIChat(chat.thread_id)
            response_message_content = openai_chat.send_message(content)
        except Exception as e:
            return self.handle_error(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR, request.user.id)

        request_message_data = dict(
            chat=chat_id,
            role='user',
            content=content
        )

        response_message_data = dict(
            chat=chat_id,
            role='assistant',
            content=response_message_content
        )

        message_pair_data = dict(
            user_message=request_message_data,
            assistant_message=response_message_data
        )

        message_pair_serializer = MessagePairSerializer(data=message_pair_data)
        message_pair_serializer.is_valid(raise_exception=True)
        message_pair_serializer.save()

        return Response(message_pair_serializer.data)
