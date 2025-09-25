from .serializers.register import RegisterSerializer
from .serializers.authenticate import AuthJWTSerializer
from .token_storage import RedisTokenStorage

from django.contrib.auth import get_user_model

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView


User = get_user_model()
storage = RedisTokenStorage()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response({"detail": "Не передан refresh-токен"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            token = RefreshToken(refresh_token)
            storage.remove_refresh_token(token["user_id"], token["jti"])
            return Response({"detail": "Вы успешно вышли"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            print("Ошибка при logout:", e)
            return Response({"detail": "Некорректный refresh-токен"}, status=status.HTTP_400_BAD_REQUEST)


class AuthTokenView(TokenObtainPairView):
    serializer_class = AuthJWTSerializer
