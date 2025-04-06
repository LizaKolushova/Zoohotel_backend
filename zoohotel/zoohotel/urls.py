from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.routers import DefaultRouter
from animals.views import *
from bookings.views import *
from hotels.views import *
from core.views import *
from notifications.views import *
from services.views import *

def show_urls(request):
    urls = []
    for url in router.urls:
        urls.append(str(url))
    return JsonResponse({"api_urls": urls})

router = DefaultRouter()
router.register(r'animal-types', AnimalTypeViewSet, basename='animaltype')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'animals', AnimalViewSet, basename='animal')
router.register(r'animal-passports', AnimalPassportViewSet, basename='animalpassport')
router.register(r'vaccinations', VaccinationViewSet, basename='vaccination')
router.register(r'treatments', TreatmentViewSet, basename='treatment')
router.register(r'bookings', BookingViewSet)
router.register(r'accommodations', AccommodationViewSet)
router.register(r'hotels', HotelViewSet)
router.register(r'hotel-restrictions', HotelRestrictionViewSet)
router.register(r'hotel-pricings', HotelPricingViewSet)
router.register(r'organizations', OrganizationViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'permissions', PermissionViewSet)
router.register(r'role-permissions', RolePermissionViewSet)
router.register(r'users', SystemUserViewSet)
router.register(r'notification-types', NotificationTypeViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'additional-services', AdditionalServiceViewSet)
router.register(r'service-records', ServiceRecordViewSet)
router.register(r'task-types', TaskTypeViewSet)
router.register(r'task-records', TaskRecordViewSet)

urlpatterns = [
    path('admin', admin.site.urls),
    path('api-urls/', show_urls),
    path('grappelli/', include('grappelli.urls')),
    path('api/', include(router.urls)),
]