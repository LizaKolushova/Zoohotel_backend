from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .models import Organization, Role, Permission, RolePermission, SystemUser
from .serializers import (
    OrganizationSerializer,
    RoleSerializer,
    PermissionSerializer,
    RolePermissionSerializer,
    SystemUserSerializer
)

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    permission_classes = [IsAuthenticated]

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]

class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]

class RolePermissionViewSet(viewsets.ModelViewSet):
    queryset = RolePermission.objects.all()
    serializer_class = RolePermissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        role_id = self.request.query_params.get('role_id')
        if role_id:
            return self.queryset.filter(role_id=role_id)
        return self.queryset

class SystemUserViewSet(viewsets.ModelViewSet):
    queryset = SystemUser.objects.all()
    serializer_class = SystemUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Для суперпользователей показываем всех пользователей
        if self.request.user.is_superuser:
            return self.queryset
        # Для остальных - только активных пользователей
        return self.queryset.filter(is_active=True)