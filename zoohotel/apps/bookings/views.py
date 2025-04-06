from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Booking, Accommodation
from .serializers import BookingSerializer, AccommodationSerializer
from rest_framework import filters

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['status', 'client__name']
    ordering_fields = ['start_date', 'end_date', 'total_price']

class AccommodationViewSet(viewsets.ModelViewSet):
    queryset = Accommodation.objects.all()
    serializer_class = AccommodationSerializer
