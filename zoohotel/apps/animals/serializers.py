from rest_framework import serializers
from .models import AnimalType, Client, Animal, AnimalPassport, Vaccination, Treatment


class AnimalTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AnimalType
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    animal_type = AnimalTypeSerializer(read_only=True)
    animal_type_id = serializers.PrimaryKeyRelatedField(
        queryset=AnimalType.objects.all(),
        source='animal_type',
        write_only=True
    )
    client = ClientSerializer(read_only=True)
    client_id = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        source='client',
        write_only=True
    )

    class Meta:
        model = Animal
        fields = '__all__'


class AnimalPassportSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(
        queryset=Animal.objects.all(),
        source='animal',
        write_only=True
    )

    class Meta:
        model = AnimalPassport
        fields = '__all__'


class VaccinationSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(
        queryset=Animal.objects.all(),
        source='animal',
        write_only=True
    )

    class Meta:
        model = Vaccination
        fields = '__all__'


class TreatmentSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(
        queryset = Animal.objects.all(),
        source = 'animal',
        write_only=True
    )

    class Meta:
        model = Treatment
        fields = '__all__'