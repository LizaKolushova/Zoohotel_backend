from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from import_export.admin import ImportExportModelAdmin
from .models import (
    AnimalType, Client, Animal, 
    AnimalPassport, Vaccination, Treatment
)

@admin.register(AnimalType)
class AnimalTypeAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    history_list_display = ['name']

@admin.register(Client)
class ClientAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'phone', 'email')
    search_fields = ('last_name', 'first_name', 'phone', 'email')
    list_filter = ('last_name',)
    ordering = ('last_name', 'first_name')
    history_list_display = ['last_name', 'first_name', 'phone', 'email']
    fieldsets = (
        ('Основная информация', {
            'fields': ('last_name', 'first_name', 'middle_name')
        }),
        ('Контактная информация', {
            'fields': ('phone', 'email')
        }),
    )

class AnimalPassportInline(admin.StackedInline):
    model = AnimalPassport
    can_delete = False
    extra = 0

class VaccinationInline(admin.TabularInline):
    model = Vaccination
    extra = 1

class TreatmentInline(admin.TabularInline):
    model = Treatment
    extra = 1

@admin.register(Animal)
class AnimalAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('name', 'animal_type', 'client', 'gender', 'birth_date', 'sterilized')
    list_filter = ('animal_type', 'gender', 'sterilized')
    search_fields = ('name', 'client__last_name', 'client__first_name', 'breed')
    ordering = ('name',)
    history_list_display = ['name', 'animal_type', 'client', 'gender', 'sterilized']
    inlines = [AnimalPassportInline, VaccinationInline, TreatmentInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('animal_type', 'client', 'name')
        }),
        ('Детали', {
            'fields': ('breed', 'birth_date', 'gender', 'weight', 'color', 'sterilized')
        }),
        ('Дополнительная информация', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )

@admin.register(AnimalPassport)
class AnimalPassportAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('animal', 'last_vet_visit')
    search_fields = ('animal__name', 'vet_visit_reason')
    list_filter = ('last_vet_visit',)
    history_list_display = ['animal', 'last_vet_visit']
    fieldsets = (
        ('Основная информация', {
            'fields': ('animal', 'last_vet_visit')
        }),
        ('Информация о здоровье', {
            'fields': ('vet_visit_reason', 'chronic_diseases', 'past_diseases')
        }),
        ('Дополнительные заметки', {
            'fields': ('vet_contact', 'health_notes'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Vaccination)
class VaccinationAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('animal', 'vaccination_name', 'vaccination_date')
    list_filter = ('vaccination_name', 'vaccination_date')
    search_fields = ('animal__name', 'vaccination_name')
    date_hierarchy = 'vaccination_date'
    ordering = ('-vaccination_date',)
    history_list_display = ['animal', 'vaccination_name', 'vaccination_date']

@admin.register(Treatment)
class TreatmentAdmin(ImportExportModelAdmin, SimpleHistoryAdmin):
    list_display = ('animal', 'treatment_type', 'treatment_date')
    list_filter = ('treatment_type', 'treatment_date')
    search_fields = ('animal__name', 'treatment_type', 'description')
    date_hierarchy = 'treatment_date'
    ordering = ('-treatment_date',)
    history_list_display = ['animal', 'treatment_type', 'treatment_date']
    fieldsets = (
        ('Основная информация', {
            'fields': ('animal', 'treatment_date', 'treatment_type')
        }),
        ('Детали', {
            'fields': ('description',),
            'classes': ('collapse',)
        }),
    )