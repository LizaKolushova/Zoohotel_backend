from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import Hotel, HotelRestriction, HotelPricing

class HotelRestrictionInline(admin.TabularInline):
    model = HotelRestriction
    extra = 1
    autocomplete_fields = ['animal_type']
    fields = ('animal_type', 'max_count')

class HotelPricingInline(admin.TabularInline):
    model = HotelPricing
    extra = 1
    fields = ('restriction', 'name', 'price')
    autocomplete_fields = ['restriction']

@admin.register(Hotel)
class HotelAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name', 'organization', 'phone', 'address_short')
    list_filter = ('organization',)
    search_fields = ('name', 'address', 'phone', 'organization__name')
    ordering = ('organization', 'name')
    history_list_display = ['name', 'organization', 'phone']
    inlines = [HotelRestrictionInline, HotelPricingInline]
    raw_id_fields = ('organization',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('organization', 'name')
        }),
        ('Контактная информация', {
            'fields': ('phone', 'address')
        }),
    )
    
    def address_short(self, obj):
        return obj.address[:50] + '...' if len(obj.address) > 50 else obj.address
    address_short.short_description = 'Адрес'

@admin.register(HotelRestriction)
class HotelRestrictionAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('hotel', 'animal_type', 'max_count')
    list_filter = ('hotel', 'animal_type')
    search_fields = ('hotel__name', 'animal_type__name')
    ordering = ('hotel', 'animal_type')
    history_list_display = ['hotel', 'animal_type', 'max_count']
    autocomplete_fields = ['hotel', 'animal_type']

@admin.register(HotelPricing)
class HotelPricingAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name', 'hotel', 'restriction', 'price')
    list_filter = ('hotel', 'restriction')
    search_fields = ('name', 'hotel__name', 'restriction__animal_type__name')
    ordering = ('hotel', 'price')
    history_list_display = ['name', 'hotel', 'price']
    raw_id_fields = ('hotel', 'restriction')
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('hotel', 'restriction', 'name')
        }),
        ('Ценообразование', {
            'fields': ('price',)
        }),
    )