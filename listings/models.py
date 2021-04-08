from django.db import models

# Create your models here.

class Listing(models.Model):
    ad_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    created_on = models.DateField()
    lat = models.DecimalField()
    lon = models.DecimalField()
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    surface_total = models.IntegerField()
    surface_covered = models.IntegerField()
    price = models.IntegerField()
    operation_type = models.CharField(max_length=100)
    proterty_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.ad_type}, {self.operation_type}, {self.address1}-{self.address2}'

        