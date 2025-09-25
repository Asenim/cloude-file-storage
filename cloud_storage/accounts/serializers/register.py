from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        min_length=2,
        max_length=150,
        help_text="Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.",
        validators=(
            UniqueValidator(queryset=User.objects.all(), message="Пользователь с таким именем уже существует."),
        ),
        error_messages={
            "required": "Имя пользователя обязательно.",
            "max_length": "Имя пользователя не может быть длиннее 150 символов.",
        }
    )
    email = serializers.EmailField(
        write_only=True,
        help_text="Обязательное поле. Введите корректный email.",
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="Пользователь с таким email уже существует.")
        ],
        error_messages={
            "required": "Email обязателен.",
            "invalid": "Введите корректный email."
        }
    )
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        help_text="Обязательное поле. Пароль должен быть не менее 8 символов.",
        error_messages={
            "required": "Пароль обязателен.",
            "min_length": "Пароль должен быть не менее 8 символов."
        }
    )
    password2 = serializers.CharField(
        write_only=True,
        min_length=8,
        help_text="Повторите пароль."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password", "password2")

    def validate(self, attrs):
        password = attrs.get("password")
        password2 = attrs.get("password2")
        if password != password2:
            raise serializers.ValidationError({"detail": "Пароли не совпадают."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        validated_data["password"] = make_password(validated_data["password"])
        return super().create(validated_data)
