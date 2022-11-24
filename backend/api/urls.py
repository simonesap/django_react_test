from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewSet, RatingViewSet
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]