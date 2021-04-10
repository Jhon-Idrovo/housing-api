from django.db import models
from listings.models import Country, Province, City, Zone, OpertationType, PropertyType
# Create your models here.

class CountryData(models.Model):
    """
    EACH DATA POINT REPRESENTS ONE MONTH
    - Each time a new listing is saved the state in the
    current month is updated if it already exist, otherwise
    a new data point is created
    - Calculations are made based on the previous state 
    and the new listing to avoid recalculations
    """
    operation_type = models.ForeignKey(OpertationType, on_delete=models.SET_NULL, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    surface_total = models.IntegerField()
    surface_covered = models.IntegerField()
    
class ProvinceData(models.Model):
    """
    EACH DATA POINT REPRESENTS ONE MONTH
    - Each time a new listing is saved the state in the
    current month is updated if it already exist, otherwise
    a new data point is created
    - Calculations are made based on the previous state 
    and the new listing to avoid recalculations
    """
    operation_type = models.ForeignKey(OpertationType, on_delete=models.SET_NULL, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    surface_total = models.IntegerField()
    surface_covered = models.IntegerField()
    
class CityData(models.Model):
    #data by location
    operation_type = models.ForeignKey(OpertationType, on_delete=models.SET_NULL, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    surface_total = models.IntegerField()
    surface_covered = models.IntegerField()
    
class ZoneData(models.Model):
    #data by location
    operation_type = models.ForeignKey(OpertationType, on_delete=models.SET_NULL, null=True)
    property_type = models.ForeignKey(PropertyType, on_delete=models.SET_NULL, null=True)
    zone = models.ForeignKey(Zone, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    rooms = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    surface_total = models.IntegerField()
    surface_covered = models.IntegerField()
