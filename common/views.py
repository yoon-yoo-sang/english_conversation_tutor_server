import logging

from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet


# Create your views here.
class BaseViewSet(GenericViewSet, ReadOnlyModelViewSet):
    @staticmethod
    def handle_error(error_message, status_code: int, user_id: int):
        logging.error({'error': error_message, 'user': user_id})
        return Response(status=status_code, data={'message': error_message})
