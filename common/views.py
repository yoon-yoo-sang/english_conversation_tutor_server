import logging

from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet


class BaseViewSet(ReadOnlyModelViewSet):
    @staticmethod
    def handle_error(error_message: str, status_code: int, user_id: int = None):
        logging.error({'error': error_message, 'user': user_id})
        return Response(status=status_code, data={'message': error_message})
