from django.db import models

class NotificationType(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Notification(models.Model):
    notification_type = models.ForeignKey(NotificationType, on_delete=models.CASCADE)
    user = models.ForeignKey(SystemUser, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)