from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EntryViewSet, ReflectionViewSet


router = DefaultRouter()

router.register('entries', EntryViewSet, basename='entry')
router.register('reflections', ReflectionViewSet, basename='reflection')


urlpatterns = [
    path('', include(router.urls)),
]