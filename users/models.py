import hashlib

from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.models import UserManager
from django.core.exceptions import MultipleObjectsReturned
from django.db import models

from common.models import BaseModel


class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        if not password:
            raise ValueError('Password is required')

        if User.objects.filter(email=email).exists():
            raise MultipleObjectsReturned('User with this email already exists')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.make_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is required')

        if not password:
            raise ValueError('Password is required')

        user = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )

        user.make_password(password)
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(BaseModel):
    REQUIRED_FIELDS = ('username', 'password')
    USERNAME_FIELD = 'email'

    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    is_anonymous = models.BooleanField(default=False)
    is_authenticated = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager()

    @property
    def is_active(self):
        return True

    @property
    def is_staff(self):
        return self.is_superuser

    def make_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    @staticmethod
    def hash_password(raw_password):
        return hashlib.sha256(raw_password.encode()).hexdigest()

    class Meta:
        db_table = 'user'
        ordering = ['created_at']

    def __str__(self):
        return self.username
