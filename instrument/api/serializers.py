from ..models import Instrument, TimeData, TemperatureData, BarometricData, PositionData, MotionData, GyroData # pylint: disable=relative-beyond-top-level
from rest_framework.serializers import Serializer, ModelSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class InstrumentSerializer(ModelSerializer):
    class Meta:
        model = Instrument
        fields = ['id', 'category', 'name', 'location', 'starred', 'position1', 'position2', 'position3'] 

class GyroDataSerializer(ModelSerializer):
    datetime = serializers.PrimaryKeyRelatedField(
        queryset=TimeData.objects.all())
    instrument = serializers.PrimaryKeyRelatedField(
        queryset=Instrument.objects.all())
    class Meta:
        model = GyroData
        fields = ['id', 'datetime', 'instrument', 'heading', 'time_string', 'instrument_name', 'date', 'time']