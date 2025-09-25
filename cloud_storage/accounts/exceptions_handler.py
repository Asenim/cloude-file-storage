from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.serializers import ValidationError


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if isinstance(exc, ValidationError) and 'detail' in exc.detail:
            response.status_code = status.HTTP_401_UNAUTHORIZED
        return response

    return response
