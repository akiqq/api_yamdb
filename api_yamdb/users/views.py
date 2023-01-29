from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView


from .serializers import (UserSerializer,
                          AdminSerializer,
                          SignUpSerializer,
                          TokenSerializer)
from .models import User
from .permissions import IsAdmin


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (
        IsAuthenticated,
        IsAdmin
    )
    lookup_field = 'username'
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_serializer_class(self):
        if (
            self.request.user.role != 'admin'
            or self.request.user.is_superuser
        ):
            return UserSerializer
        return AdminSerializer

    @action(
        detail=False,
        url_path='me',
        methods=['get', 'patch'],
        permission_classes=[IsAuthenticated, ],
        queryset=User.objects.all()
    )
    def me(self, request):
        user = get_object_or_404(User, id=request.user.id)
        if request.method == 'PATCH':
            serializer = UserSerializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data, status=HTTP_200_OK)


class SignUpView(APIView):

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.select_related('username')
        username = serializer.validated_data.get('username')
        email = serializer.validated_data.get('email')
        user, created = User.objects.get_or_create(
            username=username,
            email=email
        )
        token = default_token_generator.make_token(user)

        try:
            send_mail(
                'confirmation code',
                token,
                'from@yamdb.ru',
                [email],
                fail_silently=False,
            )
            return Response(data=serializer.data, status=HTTP_200_OK)
        except Exception:
            user.delete()
            return Response(
                status=HTTP_400_BAD_REQUEST,
            )


@api_view(http_method_names=['POST', ])
def get_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data.get('username')
    )
    confirmation_code = serializer.validated_data.get('confirmation_code')
    token = default_token_generator.check_token(user, confirmation_code)

    if token == serializer.validated_data.get('confirmation_code'):
        jwt_token = RefreshToken.for_user(user)
        return Response(
            {'token': f'{jwt_token}'}, status=HTTP_200_OK
        )
    return Response(
        status=HTTP_400_BAD_REQUEST
    )
