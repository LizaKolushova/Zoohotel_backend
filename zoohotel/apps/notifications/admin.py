from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import NotificationType, Notification

@admin.register(NotificationType)
class NotificationTypeAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    history_list_display = ['name']
    fieldsets = (
        (None, {
            'fields': ('name',),
            'description': 'Название типа уведомления'
        }),
    )
    verbose_name = "Тип уведомления"
    verbose_name_plural = "Типы уведомлений"

@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('user', 'notification_type', 'message_short', 'created_at', 'status')
    list_filter = ('notification_type', 'status', 'created_at')
    search_fields = ('user__username', 'message', 'notification_type__name')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    history_list_display = ['user', 'notification_type', 'status']
    raw_id_fields = ('user', 'notification_type')
    list_editable = ('status',)
    list_per_page = 20

    fieldsets = (
        ('Основная информация', {
            'fields': ('user', 'notification_type'),
            'description': 'Пользователь и тип уведомления'
        }),
        ('Содержимое', {
            'fields': ('message',),
            'description': 'Текст уведомления'
        }),
        ('Статус', {
            'fields': ('status',),
            'classes': ('collapse',),
            'description': 'Текущий статус уведомления'
        }),
    )

    def message_short(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_short.short_description = 'Сообщение'

    def get_readonly_fields(self, request, obj=None):
        if obj:  # редактирование существующего объекта
            return self.readonly_fields + ('created_at',)
        return self.readonly_fields
    
    verbose_name = "Уведомление"
    verbose_name_plural = "Уведомления"
