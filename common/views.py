import logging

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from common.serializers import TokenObtainPairResponseSerializer


class BaseViewSet(ReadOnlyModelViewSet):
    @staticmethod
    def handle_error(error_message: str, status_code: int, user_id: int = None):
        logging.error({'error': error_message, 'user': user_id})
        return Response(status=status_code, data={'message': error_message})


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={status.HTTP_200_OK: TokenObtainPairResponseSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
