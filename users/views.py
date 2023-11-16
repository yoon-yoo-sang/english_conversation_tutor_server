from rest_framework.viewsets import ReadOnlyModelViewSet


from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
