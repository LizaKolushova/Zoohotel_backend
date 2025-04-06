from rest_framework import serializers
from .models import NotificationType, Notification
from core.models import SystemUser
from core.serializers import SystemUserSerializer  # Импортируем сериализатор пользователя

class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = ['id', 'name']
        read_only_fields = ['id']

class NotificationSerializer(serializers.ModelSerializer):
    notification_type = NotificationTypeSerializer(read_only=True)
    notification_type_id = serializers.PrimaryKeyRelatedField(
        queryset=NotificationType.objects.all(),
        source='notification_type',
        write_only=True
    )
    user = SystemUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=SystemUser.objects.all(),
        source='user',
        write_only=True
    )

    class Meta:
        model = Notification
        fields = [
            'id', 'notification_type', 'notification_type_id', 
            'user', 'user_id', 'message', 'created_at', 'status'
        ]
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        # Дополнительные проверки данных при необходимости
        return data