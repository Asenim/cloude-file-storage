"""
Переделать под ручные роуты без использования DefaultRouter!
"""
from rest_framework.routers import DefaultRouter
from .views import UserFileViewSet

router = DefaultRouter()
router.register(r'resources', UserFileViewSet, basename='resources')

urlpatterns = router.urls
