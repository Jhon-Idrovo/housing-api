from django.contrib import admin

from .models import PropertyType, OpertationType, AddType, Listing, Country, Province, City, Zone 
# Register your models here.

admin.site.register(AddType)
admin.site.register(PropertyType)
admin.site.register(OpertationType)
admin.site.register(Listing)
admin.site.register(Country)
admin.site.register(Province)
admin.site.register(City)
admin.site.register(Zone)
