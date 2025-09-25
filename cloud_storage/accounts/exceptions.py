from rest_framework import status
from rest_framework.exceptions import APIException


class UnauthorizedException(APIException):
    """
    Пока нигде не используется
    -----------------
    Планировалось использовать в accounts/authentificate.py - AuthJWTSerializer
    Но вместо этого переопределили код ошибки в exception_handler.py и
    используем стандартную serializers.ValidationError
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Активный пользователь с такими данными не найден"
    default_code = "unauthorized"
