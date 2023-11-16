from django.db import models

from common.models import BaseModel


class Chat(BaseModel):
    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='chats'
    )
    thread_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'chat'
        ordering = ['created_at']


class Message(BaseModel):
    chat = models.ForeignKey(
        'chats.Chat',
        on_delete=models.CASCADE,
        related_name='messages'
    )
    role = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        db_table = 'message'
        ordering = ['created_at']
