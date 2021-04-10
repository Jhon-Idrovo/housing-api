from django.db import models

#UBICATION RELATED MODELS--------------------------------
class Country(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name



class Province(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name



class City(models.Model):
    name = models.CharField(max_length=50)
    province = models.ForeignKey(Province, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name



class Zone(models.Model):
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


#LISTING TYPES REALATED--------------------------------------------
class OpertationType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class PropertyType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class AddType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Listing(models.Model):
    ad_type = models.ForeignKey(AddType, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateField()
    lat = models.DecimalField(decimal_places=8, max_digits=14)
    lon = models.DecimalField(decimal_places=8, max_digits=14)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    surface_total = models.IntegerField()
    surface_covered = models.IntegerField()
    price = models.IntegerField()
    operation_type = models.ForeignKey(OpertationType, on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ad_type.name}, {self.operation_type.name}, {self.country.name}-{self.province.name}'

        