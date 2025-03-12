from django.db import models
from core.models import Organization

class Hotel(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=20)

class HotelRestriction(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    animal_type = models.ForeignKey('animals.AnimalType', on_delete=models.CASCADE)
    max_count = models.PositiveIntegerField()

class HotelPricing(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    restriction = models.ForeignKey(HotelRestriction, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

