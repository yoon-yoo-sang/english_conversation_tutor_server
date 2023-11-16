from django.db import models

from common.models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'
        ordering = ['created_at']

    def __str__(self):
        return self.name
