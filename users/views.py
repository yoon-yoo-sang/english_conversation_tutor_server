from django.core.exceptions import MultipleObjectsReturned
from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from common.serializers import EmptySerializer
from common.views import BaseViewSet
from config.authenticate import CustomAuthenticated
from users.models import User
from users.serializers import UserSerializer, SignUpSerializer


class UserViewSet(BaseViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [AllowAny, ]
        else:
            self.permission_classes = [CustomAuthenticated, ]

        return super(UserViewSet, self).get_permissions()

    @swagger_auto_schema(
        request_body=SignUpSerializer,
        responses={status.HTTP_201_CREATED: EmptySerializer}
    )
    @transaction.atomic
    @action(methods=['post'], detail=False)
    def sign_up(self, request, *args, **kwargs):
        try:
            serializer = SignUpSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except MultipleObjectsReturned:
            return self.handle_error('User with this email already exists', status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return self.handle_error('Email and password are required', status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return self.handle_error(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(status=status.HTTP_201_CREATED)
