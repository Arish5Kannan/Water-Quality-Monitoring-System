from django.contrib import admin
from aquanet.models import *
# Register your models here.
admin.site.register(realtime)
admin.site.register(User)
admin.site.register(PHReading)
admin.site.register(TemperatureReading)
admin.site.register(TurbidityReading)
admin.site.register(ConductivityReading)