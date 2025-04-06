from rest_framework import serializers
from .models import Hotel, HotelRestriction, HotelPricing
from animals.models import AnimalType
from animals.serializers import AnimalTypeSerializer

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['id', 'organization', 'name', 'address', 'phone']
        read_only_fields = ['id']

class HotelRestrictionSerializer(serializers.ModelSerializer):
    animal_type = AnimalTypeSerializer(read_only=True)
    animal_type_id = serializers.PrimaryKeyRelatedField(
        queryset = AnimalType.objects.all(),
        source='animal_type',
        write_only=True
    )

    class Meta:
        model = HotelRestriction
        fields = ['id', 'hotel', 'animal_type', 'animal_type_id', 'max_count']
        read_only_fields = ['id']

class HotelPricingSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelPricing
        fields = ['id', 'hotel', 'restriction', 'name', 'price']
        read_only_fields = ['id']

    def validate(self, data):
        if data['restriction'].hotel != data['hotel']:
            raise serializers.ValidationError("Restriction must belong to the same hotel")
        return data