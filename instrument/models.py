from django.db import models
from django.db.models import Model, CharField, ForeignKey, FloatField, DecimalField, TextField, DateTimeField, IntegerField, OneToOneField
# Create your models here.
class Instrument(Model):
    SENSOR_CHOICES = [
        ('gyro', 'Gyro'),
        ('motion', 'Motion'),
        ('position', 'Position'),
        ('temperature', 'Temperature'),
        ('barometric', 'Barometric'),
    ]
    category = CharField(max_length=32, choices=SENSOR_CHOICES, help_text='Enter the measurement category')
    name = CharField(max_length=32, help_text='Enter instrument name.')
    location = CharField(max_length=32, help_text='Enter instrument location.', null=True)
    starred = models.BooleanField(default=False)
    position1 = IntegerField(null=True, blank=True, unique=True)
    position2 = IntegerField(null=True, blank=True, unique=True)
    position3 = IntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name


def check_digits(time_string):
    if len(time_string) == 1:
        return '0' + time_string
    return time_string

def make_time_key(time):
    day = check_digits(str(time.day))
    month = check_digits(str(time.month))
    hour = check_digits(str(time.hour))
    minute = check_digits(str(time.minute))
    second = check_digits(str(time.second))
    year = str(time.year)
    return year + month + day + hour + minute + second

class TimeData(Model):
    datetime = DateTimeField()
    def time(self):
        return check_digits(str(self.datetime.hour)) + ':' + check_digits(str(self.datetime.minute))
    def date(self):
        return str(self.datetime.year) + '/' + check_digits(str(self.datetime.month)) + '/' + check_digits(str(self.datetime.day))
    def __str__(self):
        return make_time_key(self.datetime)

class GyroData(Model):
    instrument = ForeignKey('Instrument', related_name='gyro_instrument', on_delete=models.CASCADE)
    datetime = OneToOneField('TimeData', related_name='gyro_time', on_delete=models.CASCADE)
    heading = DecimalField(decimal_places=3, max_digits=20, )
    def __str__(self):
        return str(self.heading)
    def time_string(self):
        return str(self.datetime)
    def instrument_name(self):
        return str(self.instrument)
    def date(self):
        return self.datetime.date()
    def time(self):
        return self.datetime.time()

class MotionData(Model):
    instrument = ForeignKey('Instrument', related_name='motion_instrument', on_delete=models.CASCADE)
    time = OneToOneField('TimeData', related_name='motion_time', on_delete=models.CASCADE)
    pitch = DecimalField(decimal_places=3, max_digits=20, null=True)
    roll = DecimalField(decimal_places=3, max_digits=20, null=True)
    heave = DecimalField(decimal_places=3, max_digits=20, null=True)

class PositionData(Model):
    instrument = ForeignKey('Instrument', related_name='position_instrument', on_delete=models.CASCADE)
    time = OneToOneField('TimeData', related_name='position_time', on_delete=models.CASCADE)
    easting = DecimalField(decimal_places=3, max_digits=20, null=True)
    northing = DecimalField(decimal_places=3, max_digits=20, null=True)
    height = DecimalField(decimal_places=3, max_digits=20, null=True)

class TemperatureData(Model):
    instrument = ForeignKey('Instrument', related_name='temperature_instrument', on_delete=models.CASCADE)
    time = OneToOneField('TimeData', related_name='temperature_time', on_delete=models.CASCADE)
    temperature = DecimalField(decimal_places=3, max_digits=20, null=True)

class BarometricData(Model):
    instrument = ForeignKey('Instrument', related_name='barometric_instrument', on_delete=models.CASCADE)
    time = OneToOneField('TimeData', related_name='barometric_time', on_delete=models.CASCADE)
    Barometric = DecimalField(decimal_places=3, max_digits=20, null=True)
