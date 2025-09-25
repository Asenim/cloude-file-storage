from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework import serializers

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from ..token_storage import RedisTokenStorage


storage = RedisTokenStorage()


class AuthJWTSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, max_length=150)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        # Важно: сначала базовая валидация полей
        attrs = super().validate(attrs)

        username = attrs.get("username")
        password = attrs.get("password")
        password2 = attrs.get("password2")

        if password != password2:
            raise serializers.ValidationError(
                {"detail": "Пароли не совпадают."}
            )

        user = authenticate(username=username, password=password)
        if not user:
            raise serializers.ValidationError({
                "detail": _("Активный пользователь с такими данными не найден")
            })

        refresh = RefreshToken.for_user(user)

        refresh_user_id = refresh["user_id"]
        refresh_jti = refresh["jti"]

        storage.save_refresh_token(
            user_id=refresh_user_id,
            jti=refresh_jti,
            token=str(refresh),
            exp_seconds=refresh.lifetime.total_seconds()
        )

        return {
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }
