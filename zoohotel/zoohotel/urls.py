"""zoohotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from apps.animals.views import *

router = DefaultRouter()
router.register(r'animal-types', AnimalTypeViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'animals', AnimalViewSet)
router.register(r'animal-passports', AnimalPassportViewSet)
router.register(r'vaccinations', VaccinationViewSet)
router.register(r'treatments', TreatmentViewSet)


urlpatterns = [
    path('', admin.site.urls),
    path('grappelli/', include('grappelli.urls')),
    path('api/', include(router.urls)),
]
