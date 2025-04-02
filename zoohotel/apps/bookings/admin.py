from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Booking, Accommodation

class AccommodationInline(admin.TabularInline):
    model = Accommodation
    extra = 0
    fields = ('animal', 'check_in_date', 'check_out_date')
    raw_id_fields = ('animal',)
    show_change_link = True

@admin.register(Booking)
class BookingAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('id', 'client', 'hotel', 'start_date', 'end_date', 'status', 'total_price')
    list_filter = ('status', 'hotel', 'start_date', 'end_date')
    search_fields = ('client__last_name', 'client__first_name', 'hotel__name', 'pricing__name')
    date_hierarchy = 'start_date'
    ordering = ('-start_date',)
    history_list_display = ['client', 'hotel', 'status', 'total_price']
    inlines = [AccommodationInline]
    raw_id_fields = ('client', 'hotel', 'pricing')
    fieldsets = (
        ('Основная информация', {
            'fields': ('client', 'hotel', 'pricing', ('start_date', 'end_date'))
        }),
        ('Статус и стоимость', {
            'fields': ('status', 'total_price')
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # редактирование существующего объекта
            return self.readonly_fields + ('client', 'hotel', 'pricing', 'start_date', 'end_date')
        return self.readonly_fields

@admin.register(Accommodation)
class AccommodationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('booking', 'animal', 'check_in_date', 'check_out_date')
    list_filter = ('check_in_date', 'check_out_date')
    search_fields = ('animal__name', 'booking__client__last_name', 'booking__hotel__name')
    date_hierarchy = 'check_in_date'
    ordering = ('-check_in_date',)
    history_list_display = ['booking', 'animal', 'check_in_date']
    raw_id_fields = ('animal', 'booking')
    fieldsets = (
        ('Основная информация', {
            'fields': ('booking', 'animal')
        }),
        ('Даты', {
            'fields': (('check_in_date', 'check_out_date'),)
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # редактирование существующего объекта
            return self.readonly_fields + ('booking', 'animal')
        return self.readonly_fields
