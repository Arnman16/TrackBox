from django.urls import path, include
from rest_framework import routers
from .viewsets import InstrumentViewSet, GyroDataViewSet


router = routers.DefaultRouter()
router.register(r'instruments', InstrumentViewSet)
router.register(r'gyrodata', GyroDataViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
