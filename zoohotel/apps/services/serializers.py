from rest_framework import serializers
from .models import AdditionalService, ServiceRecord, TaskType, TaskRecord
from animals.models import Animal
from core.models import SystemUser
from animals.serializers import AnimalSerializer
from core.serializers import SystemUserSerializer

class AdditionalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalService
        fields = ['id', 'name', 'description', 'price']
        read_only_fields = ['id']

class ServiceRecordSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(
        queryset=Animal.objects.all(),
        source='animal',
        write_only=True
    )
    user = SystemUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=SystemUser.objects.all(),
        source='user',
        write_only=True
    )

    class Meta:
        model = ServiceRecord
        fields = [
            'id', 'animal', 'animal_id', 'user', 'user_id',
            'service_date', 'service_time', 'repeat_count', 'notes'
        ]
        read_only_fields = ['id']

class TaskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskType
        fields = ['id', 'name', 'description', 'category', 'duration']
        read_only_fields = ['id']

class TaskRecordSerializer(serializers.ModelSerializer):
    user = SystemUserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=SystemUser.objects.all(),
        source='user',
        write_only=True
    )
    task_type = TaskTypeSerializer(read_only=True)
    task_type_id = serializers.PrimaryKeyRelatedField(
        queryset=TaskType.objects.all(),
        source='task_type',
        write_only=True
    )

    class Meta:
        model = TaskRecord
        fields = [
            'id', 'user', 'user_id', 'task_type', 'task_type_id',
            'task_date', 'task_time', 'repeat_count', 'notes'
        ]
        read_only_fields = ['id']