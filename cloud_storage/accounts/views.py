from rest_framework import generics
from .serializers.register import RegisterSerializer
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterView(generics.CreateAPIView):
    # Указываем с каким queryset работаем
    queryset = User.objects.all()
    # Указываем с каким сериализатором взаимодействуем
    serializer_class = RegisterSerializer
