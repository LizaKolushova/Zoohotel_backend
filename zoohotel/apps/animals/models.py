from django.db import models

class AnimalType(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Client(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True, blank=True, null=True)

class Animal(models.Model):
    animal_type = models.ForeignKey(AnimalType, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    color = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    sterilized = models.BooleanField()

class AnimalPassport(models.Model):
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    last_vet_visit = models.DateField(blank=True, null=True)
    vet_visit_reason = models.TextField(blank=True, null=True)
    chronic_diseases = models.TextField(blank=True, null=True)
    past_diseases = models.TextField(blank=True, null=True)
    vet_contact = models.TextField(blank=True, null=True)
    health_notes = models.TextField(blank=True, null=True)

class Vaccination(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    vaccination_date = models.DateField()
    vaccination_name = models.CharField(max_length=255)

class Treatment(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    treatment_date = models.DateField()
    treatment_type = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
