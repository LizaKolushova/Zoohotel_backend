from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Hotel, HotelRestriction, HotelPricing
from .serializers import HotelSerializer, HotelRestrictionSerializer, HotelPricingSerializer

class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    permission_classes = [IsAuthenticated]

class HotelRestrictionViewSet(viewsets.ModelViewSet):
    queryset = HotelRestriction.objects.all()
    serializer_class = HotelRestrictionSerializer
    permission_classes = [IsAuthenticated]

class HotelPricingViewSet(viewsets.ModelViewSet):
    queryset = HotelPricing.objects.all()
    serializer_class = HotelPricingSerializer
    permission_classes = [IsAuthenticated]
