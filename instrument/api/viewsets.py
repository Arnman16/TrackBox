from rest_framework.viewsets import ModelViewSet, GenericViewSet
from ..models import Instrument, TimeData, TemperatureData, BarometricData, PositionData, MotionData, GyroData # pylint: disable=relative-beyond-top-level
from django.contrib.auth import get_user_model
from .serializers import InstrumentSerializer, GyroDataSerializer # pylint: disable=relative-beyond-top-level
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin


class InstrumentViewSet(RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = Instrument.objects.all().order_by('category')
    test = Instrument.objects.all()
    serializer_class = InstrumentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'category', 'starred'
    ]

class GyroDataViewSet(RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = GyroData.objects.all().order_by('datetime')
    serializer_class = GyroDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'instrument'
    ]

