from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.settings import api_settings

from config.settings import DEBUG
from users.models import User


class CustomAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated)


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user_id = validated_token[api_settings.USER_ID_CLAIM]
        user = User.objects.get(id=user_id)

        if type(user) is AnonymousUser and DEBUG:
            admin_user = User.objects.filter(is_superuser=True).first()
            return admin_user

        if user.is_active:
            return user

        return None
