from django.db import models
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


def user_directory_path(instance, filename):
    """
    Генерируем или получаем путь к файлу в бакете
    Используется с UserFile
    :param instance: это объект модели UserFile, который сейчас сохраняется
    :param filename: исходное имя файла, которое загружает пользователь
    :return:
    """
    return f"{instance.user.username}/{filename}"


class UserFileStorage(S3Boto3Storage):
    """
    Attributes:
        location: Это префикс (папка) внутри бакета, куда будут сохраняться файлы.
    """
    location = ''


class UserFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(storage=UserFileStorage(), upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
