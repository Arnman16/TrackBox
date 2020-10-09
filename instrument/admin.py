from django.contrib import admin
from .models import Instrument
from .models import GyroData
from .models import TimeData


# Register your models here.
admin.site.register(Instrument)
admin.site.register(GyroData)
admin.site.register(TimeData)