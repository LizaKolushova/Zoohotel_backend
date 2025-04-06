from django.db import models
from core.models import SystemUser
from animals.models import Animal

class AdditionalService(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'additional_services'
        verbose_name = 'Дополнительная услуга'
        verbose_name_plural = 'Дополнительные услуги'


class ServiceRecord(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    service_date = models.DateField()
    service_time = models.TimeField()
    repeat_count = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'service_records'
        verbose_name = 'Запись услуги'
        verbose_name_plural = 'Записи услуг'
        indexes = [
            models.Index(fields=['service_date', 'service_time']),
            models.Index(fields=['animal']),
        ]


class TaskType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()

    class Meta:
        db_table = 'task_types'
        verbose_name = 'Тип задачи'
        verbose_name_plural = 'Типы задач'
        ordering = ['category', 'name']


class TaskRecord(models.Model):
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    task_date = models.DateField()
    task_time = models.TimeField()
    repeat_count = models.PositiveIntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'task_records'
        verbose_name = 'Запись задачи'
        verbose_name_plural = 'Записи задач'
        indexes = [
            models.Index(fields=['task_date', 'task_time']),
            models.Index(fields=['user']),
        ]