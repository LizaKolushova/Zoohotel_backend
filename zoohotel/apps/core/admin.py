from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import Group
from .models import Organization, Role, Permission, RolePermission, SystemUser

@admin.register(Organization)
class OrganizationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    ordering = ('name',)
    history_list_display = ['name', 'email']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'email')
        }),
    )

class RolePermissionInline(admin.TabularInline):
    model = RolePermission
    extra = 1
    autocomplete_fields = ['permission']

@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)
    history_list_display = ['name']
    inlines = [RolePermissionInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description')
        }),
    )

@admin.register(Permission)
class PermissionAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)
    history_list_display = ['name']
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'content_type', 'description')
        }),
    )

@admin.register(RolePermission)
class RolePermissionAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('role', 'permission')
    search_fields = ('role__name', 'permission__name')
    list_filter = ('role', 'permission')
    history_list_display = ['role', 'permission']
    autocomplete_fields = ['role', 'permission']

@admin.register(SystemUser)
class CustomUserAdmin(UserAdmin, ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_role', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'role__name')
    ordering = ('username',)
    history_list_display = ['username', 'email', 'get_role']
    
    fieldsets = (
        ('Основная информация', {'fields': ('username', 'password')}),
        ('Личная информация', {'fields': ('first_name', 'last_name', 'email', 'phone', 'role')}),
        ('Разрешения', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Важные даты', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        ('Создание пользователя', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role'),
        }),
    )
    
    filter_horizontal = ('groups', 'user_permissions',)
    
    def get_role(self, obj):
        return obj.role.name if obj.role else None
    get_role.short_description = 'Роль'
    get_role.admin_order_field = 'role__name'

# Отменяем регистрацию стандартной группы, если нужно
admin.site.unregister(Group)
