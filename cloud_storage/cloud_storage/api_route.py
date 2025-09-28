from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import get_resolver
from django.urls import reverse, NoReverseMatch


@api_view(['GET'])
def custom_api_root(request, format=None):
    # Получаем всю карту url проекта
    resolver = get_resolver()
    url_dict = {}

    for name, url_pattern in resolver.reverse_dict.items():
        if isinstance(name, str):
            try:
                # build_absolute_uri вернет полный URL
                url_dict[name] = request.build_absolute_uri(reverse(name))
            except NoReverseMatch:
                # пропускаем урлы, которые требуют аргументы
                continue

    return Response(url_dict)
