from django.contrib.auth.models import AnonymousUser
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from config.settings import DEBUG
from users.models import User


class CustomAuthenticated(IsAuthenticated):
    def has_permission(self, request, view):
        if DEBUG:
            return True
        return bool(request.user and request.user.is_authenticated)


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        user = super().get_user(validated_token)

        if type(user) is AnonymousUser and DEBUG:
            admin_user = User.objects.filter(is_superuser=True).first()
            return admin_user

        if user.is_active:
            return user

        return None
