from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import AdditionalService, ServiceRecord, TaskType, TaskRecord

@admin.register(AdditionalService)
class AdditionalServiceAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name', 'price', 'description')
    search_fields = ('name', 'description')
    list_filter = ('price',)
    ordering = ('name',)
    history_list_display = ['name', 'price']
    fieldsets = (
        (None, {
            'fields': ('name', 'price')
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )

class ServiceRecordInline(admin.TabularInline):
    model = ServiceRecord
    extra = 0
    fields = ('service_date', 'service_time', 'user', 'repeat_count')
    readonly_fields = ('user',)

@admin.register(ServiceRecord)
class ServiceRecordAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('animal', 'service_date', 'service_time', 'user', 'repeat_count')
    search_fields = ('animal__name', 'notes', 'user__username')
    list_filter = ('service_date', 'user')
    date_hierarchy = 'service_date'
    ordering = ('-service_date', '-service_time')
    history_list_display = ['animal', 'service_date', 'user']
    fieldsets = (
        (None, {
            'fields': ('animal', 'user', ('service_date', 'service_time'))
        }),
        ('Details', {
            'fields': ('repeat_count', 'notes'),
            'classes': ('collapse',)
        }),
    )
    raw_id_fields = ('animal', 'user')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

@admin.register(TaskType)
class TaskTypeAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name', 'category', 'duration', 'description')
    search_fields = ('name', 'category', 'description')
    list_filter = ('category', 'duration')
    ordering = ('category', 'name')
    history_list_display = ['name', 'category', 'duration']
    fieldsets = (
        (None, {
            'fields': ('name', 'category', 'duration')
        }),
        ('Description', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )

@admin.register(TaskRecord)
class TaskRecordAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('task_type', 'task_date', 'task_time', 'user', 'repeat_count')
    search_fields = ('task_type__name', 'notes', 'user__username')
    list_filter = ('task_date', 'task_type', 'user')
    date_hierarchy = 'task_date'
    ordering = ('-task_date', '-task_time')
    history_list_display = ['task_type', 'task_date', 'user']
    fieldsets = (
        (None, {
            'fields': ('task_type', 'user', ('task_date', 'task_time'))
        }),
        ('Details', {
            'fields': ('repeat_count', 'notes'),
            'classes': ('collapse',)
        }),
    )
    raw_id_fields = ('user', 'task_type')

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)