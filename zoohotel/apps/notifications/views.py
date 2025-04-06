from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import NotificationType, Notification
from .serializers import NotificationTypeSerializer, NotificationSerializer
from django_filters.rest_framework import DjangoFilterBackend

class NotificationTypeViewSet(viewsets.ModelViewSet):
    queryset = NotificationType.objects.all()
    serializer_class = NotificationTypeSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'notification_type', 'status']
    ordering_fields = ['created_at']
    ordering = ['-created_at']  

    def get_queryset(self):
        """
        Показываем только уведомления текущего пользователя,
        кроме случаев, когда пользователь - администратор
        """
        user = self.request.user
        queryset = super().get_queryset()
        
        if not user.is_staff:
            queryset = queryset.filter(user=user)
        
        return queryset

    @action(detail=True, methods=['post'])
    def mark_as_read(self, request, pk=None):
        """Эндпоинт для отметки уведомления как прочитанного"""
        notification = self.get_object()
        notification.status = True
        notification.save()
        return Response({'status': 'notification marked as read'})

    @action(detail=False, methods=['post'])
    def mark_all_as_read(self, request):
        """Эндпоинт для отметки всех уведомлений как прочитанных"""
        queryset = self.filter_queryset(self.get_queryset())
        queryset.update(status=True)
        return Response({'status': 'all notifications marked as read'})