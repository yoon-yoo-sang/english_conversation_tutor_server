from rest_framework import serializers

from chats.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = (
            'id',
            'user',
            'thread_id',
        )


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'id',
            'created_at',
            'updated_at',
            'chat',
            'role',
            'content',
        )


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            'chat',
            'content',
        )


class MessagePairSerializer(serializers.Serializer):
    user_message = MessageSerializer()
    assistant_message = MessageSerializer()

    def save(self, **kwargs):
        user_message_data = self.validated_data['user_message']
        assistant_message_data = self.validated_data['assistant_message']
        user_message = Message.objects.create(
            chat=user_message_data['chat'],
            role=user_message_data['role'],
            content=user_message_data['content'],
        )
        assistant_message = Message.objects.create(
            chat=assistant_message_data['chat'],
            role=assistant_message_data['role'],
            content=assistant_message_data['content'],
        )
        return {
            'user_message': user_message,
            'assistant_message': assistant_message,
        }
