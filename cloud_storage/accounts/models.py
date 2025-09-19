from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUsers(AbstractUser):
    username = models.CharField(error_messages={
        'unique': "Пользователь с таким именем уже существует.",
    }, unique=True, null=False
    )
    email = models.EmailField(blank=False, unique=True, null=False)
    password = models.CharField(null=False)
