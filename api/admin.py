from django.contrib import admin
from .models import CountryData, ProvinceData, CityData, ZoneData

# Register your models here.
admin.site.register(CountryData)
admin.site.register(ProvinceData)
admin.site.register(CityData)
admin.site.register(ZoneData)