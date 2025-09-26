from django.db import models
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class UserFileStorage(S3Boto3Storage):
    # Это префикс (папка) внутри бакета, куда будут сохраняться файлы.
    location = 'resource'


class UserFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    file = models.FileField(storage=UserFileStorage())
    uploaded_at = models.DateTimeField(auto_now_add=True)
