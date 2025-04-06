from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .models import AdditionalService, ServiceRecord, TaskType, TaskRecord
from .serializers import (
    AdditionalServiceSerializer,
    ServiceRecordSerializer,
    TaskTypeSerializer,
    TaskRecordSerializer
)

class AdditionalServiceViewSet(viewsets.ModelViewSet):
    queryset = AdditionalService.objects.all()
    serializer_class = AdditionalServiceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description']
    filterset_fields = ['price']

class ServiceRecordViewSet(viewsets.ModelViewSet):
    queryset = ServiceRecord.objects.all()
    serializer_class = ServiceRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['animal', 'user', 'service_date']
    ordering_fields = ['service_date', 'service_time']
    ordering = ['-service_date', '-service_time']

    # def get_queryset(self):
    #     """Фильтрация записей для обычных пользователей"""
    #     user = self.request.user
    #     if not user.is_staff:
    #         return self.queryset.filter(user=user)
    #     return self.queryset

class TaskTypeViewSet(viewsets.ModelViewSet):
    queryset = TaskType.objects.all()
    serializer_class = TaskTypeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ['name', 'description', 'category']
    filterset_fields = ['category', 'duration']

class TaskRecordViewSet(viewsets.ModelViewSet):
    queryset = TaskRecord.objects.all()
    serializer_class = TaskRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['user', 'task_type', 'task_date']
    ordering_fields = ['task_date', 'task_time']
    ordering = ['-task_date', '-task_time']

    # def get_queryset(self):
    #     """Фильтрация записей задач для обычных пользователей"""
    #     user = self.request.user
    #     if not user.is_staff:
    #         return self.queryset.filter(user=user)
    #     return self.queryset