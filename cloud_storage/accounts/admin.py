from django.contrib import admin
from .models import BaseUsers

# Регистрируем нашу модель юзера в админке
admin.site.register(BaseUsers)
