from django.urls import path, include
from rest_framework import routers
from .views import BookViewSet, CharacterViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)
router.register('characters', CharacterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]