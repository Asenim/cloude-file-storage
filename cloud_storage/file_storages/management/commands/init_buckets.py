import boto3
from django.core.management.base import BaseCommand

from django.conf import settings


class Command(BaseCommand):
    help = "Создаёт S3 бакет если его нет"

    def handle(self, *args, **kwargs):
        s3 = boto3.client(
            "s3",
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
            aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        try:
            s3.create_bucket(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
            self.stdout.write(self.style.SUCCESS("Бакет создан"))
        except s3.exceptions.BucketAlreadyOwnedByYou:
            self.stdout.write(self.style.WARNING("Бакет уже существует"))
