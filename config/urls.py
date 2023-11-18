from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from chats.views import ChatViewSet, MessageViewSet
from common.views import DecoratedTokenObtainPairView
from config.settings import DEBUG
from users.views import UserViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', DecoratedTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if DEBUG:
    schema_view = get_schema_view(
        openapi.Info(
            title="English Conversation Tutor API",
            default_version='v1',
            description="API specification for English Conversation Tutor",
            terms_of_service="https://www.google.com/policies/terms/",
            contact=openapi.Contact(email="yysss61888@gmail.com"),
            license=openapi.License(name="BSD License"),
        ),
        public=True,
    )

    urlpatterns += [
        path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
