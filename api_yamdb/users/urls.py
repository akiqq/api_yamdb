from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import SignUpView, get_token, UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet, basename='users')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/auth/token/', get_token, name='token'),
    path('api/v1/auth/signup/', SignUpView.as_view(), name='signup'),
]
