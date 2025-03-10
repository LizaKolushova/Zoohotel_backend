from django.db import models
from django.contrib.auth.models import AbstractUser

# core/models.py
class Organization(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

class Role(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

class Permission(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

class RolePermission(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

class SystemUser(AbstractUser):
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.SET_NULL)
    phone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

