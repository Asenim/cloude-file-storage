from django.contrib.auth.models import AbstractUser
from django.db import models


class BaseUsers(AbstractUser):
    email = models.EmailField(blank=False, unique=True, null=False)
