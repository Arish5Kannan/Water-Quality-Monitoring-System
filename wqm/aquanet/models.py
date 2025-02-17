from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    contact_no = models.CharField(max_length=15, blank=True, null=True)
class BaseReading(models.Model):
    reading = models.FloatField(blank=False, null=False, default=0)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    class Meta:
        abstract = True  # This class won't create a separate table

class PHReading(BaseReading):
    threshold_min = models.FloatField(default=6.5)  # Minimum pH threshold
    threshold_max = models.FloatField(default=8.5)  # Maximum pH threshold

class TemperatureReading(BaseReading):
    threshold_min = models.FloatField(default=0.0)  # Minimum temperature in Celsius
    threshold_max = models.FloatField(default=30.0)  # Maximum temperature in Celsius

class ConductivityReading(BaseReading):
    threshold_min = models.FloatField(default=50.0)  # Minimum conductivity in µS/cm
    threshold_max = models.FloatField(default=1500.0)  # Maximum conductivity in µS/cm

class TurbidityReading(BaseReading):
    threshold_min = models.FloatField(default=0.0)  # Minimum turbidity in NTU
    threshold_max = models.FloatField(default=5.0)  # Maximum turbidity in NTU
class realtime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    ph = models.FloatField(blank=False, null=False, default=0)
    temperature = models.FloatField(blank=False, null=False, default=0)
    conductivity = models.FloatField(blank=False, null=False, default=0)
    turbidity = models.FloatField(blank=False, null=False, default=0) 
