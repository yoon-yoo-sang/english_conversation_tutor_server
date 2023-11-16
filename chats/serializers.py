from rest_framework import serializers

from chats.models import Chat


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
        model = Chat
        fields = (
            'id',
            'chat',
            'role',
            'content',
        )
