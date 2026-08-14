from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import EntryViewSet, ReflectionViewSet
from .views import home
from .views import home, entries_page


router = DefaultRouter()

router.register('entries', EntryViewSet, basename='entry')
router.register('reflections', ReflectionViewSet, basename='reflection')


urlpatterns = [
    path('', include(router.urls)),
    path('', home, name='home'),
    path('entries/', entries_page, name='entries'),

]