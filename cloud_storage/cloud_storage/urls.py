from django.contrib import admin
from django.urls import path, include
from .api_route import custom_api_root


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', custom_api_root, name='api-route'),
    path('api/', include('accounts.urls')),
    path('api/', include('file_storages.urls'))
]
