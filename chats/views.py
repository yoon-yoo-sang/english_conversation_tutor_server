from rest_framework.viewsets import ReadOnlyModelViewSet


from chats.models import Chat, Message
from chats.serializers import ChatSerializer, MessageSerializer


class ChatViewSet(ReadOnlyModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class MessageViewSet(ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
