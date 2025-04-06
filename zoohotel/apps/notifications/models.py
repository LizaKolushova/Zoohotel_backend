from django.db import models
from core.models import SystemUser

class NotificationType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = 'notification_types'
        verbose_name = 'Тип уведомления'
        verbose_name_plural = 'Типы уведомлений'


class Notification(models.Model):
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['user', 'status']),  # составной индекс
        ]