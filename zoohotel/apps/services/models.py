from django.db import models

class AdditionalService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ServiceRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_time = models.TimeField()
    repeat_count = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

class TaskType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()

class TaskRecord(models.Model):
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    task_date = models.DateField()
    task_time = models.TimeField()
    repeat_count = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
