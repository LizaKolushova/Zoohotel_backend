from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import AnimalType, Client, Animal, AnimalPassport, Vaccination, Treatment
from .serializers import (
    AnimalTypeSerializer,
    ClientSerializer,
    AnimalSerializer,
    AnimalPassportSerializer,
    VaccinationSerializer,
    TreatmentSerializer
)



class AnimalTypeViewSet(viewsets.ModelViewSet):
    queryset = AnimalType.objects.all()
    serializer_class = AnimalTypeSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    @action(detail=True, methods=['get'])
    def animals(self, request, pk=None):
        """
        Получение списка животных клиента
        """
        client = get_object_or_404(Client.objects.all(), pk=pk)
        animals = Animal.objects.filter(client=client)
        serializer = AnimalSerializer(animals, many=True)
        return Response(serializer.data)

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer

    @action(detail=True, methods=['get'])
    def passport(self, request, pk=None):
        animal = get_object_or_404(Animal.objects.all(), pk=pk)
        passport = get_object_or_404(AnimalPassport.objects.all(), animal=animal)
        serializer = AnimalPassportSerializer(passport)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def vaccinations(self, request, pk=None):
        animal = get_object_or_404(Animal.objects.all(), pk=pk)
        vaccinations = Vaccination.objects.filter(animal=animal)
        serializer = VaccinationSerializer(vaccinations, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def treatments(self, request, pk=None):
        animal = get_object_or_404(Animal.objects.all(), pk=pk)
        treatments = Treatment.objects.filter(animal=animal)
        serializer = TreatmentSerializer(treatments, many=True)
        return Response(serializer.data)

class AnimalPassportViewSet(viewsets.ModelViewSet):
    queryset = AnimalPassport.objects.all()
    serializer_class = AnimalPassportSerializer

class VaccinationViewSet(viewsets.ModelViewSet):
    queryset = Vaccination.objects.all()
    serializer_class = VaccinationSerializer

class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


# class AnimalTypeViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet для работы с типами животных
#     """
#     def list(self, request):
#         queryset = AnimalType.objects.all()
#         serializer = AnimalTypeSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = AnimalTypeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = AnimalType.objects.all()
#         animal_type = get_object_or_404(queryset, pk=pk)
#         serializer = AnimalTypeSerializer(animal_type)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         animal_type = get_object_or_404(AnimalType.objects.all(), pk=pk)
#         serializer = AnimalTypeSerializer(animal_type, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         animal_type = get_object_or_404(AnimalType.objects.all(), pk=pk)
#         serializer = AnimalTypeSerializer(animal_type, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         animal_type = get_object_or_404(AnimalType.objects.all(), pk=pk)
#         animal_type.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ClientViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet для работы с клиентами
#     """
#     def list(self, request):
#         queryset = Client.objects.all()
#         serializer = ClientSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ClientSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Client.objects.all()
#         client = get_object_or_404(queryset, pk=pk)
#         serializer = ClientSerializer(client)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         client = get_object_or_404(Client.objects.all(), pk=pk)
#         serializer = ClientSerializer(client, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         client = get_object_or_404(Client.objects.all(), pk=pk)
#         serializer = ClientSerializer(client, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         client = get_object_or_404(Client.objects.all(), pk=pk)
#         client.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     @action(detail=True, methods=['get'])
#     def animals(self, request, pk=None):
#         """
#         Получение списка животных клиента
#         """
#         client = get_object_or_404(Client.objects.all(), pk=pk)
#         animals = Animal.objects.filter(client=client)
#         serializer = AnimalSerializer(animals, many=True)
#         return Response(serializer.data)


# class AnimalViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet для работы с животными
#     """
#     def list(self, request):
#         queryset = Animal.objects.all()
#         serializer = AnimalSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = AnimalSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Animal.objects.all()
#         animal = get_object_or_404(queryset, pk=pk)
#         serializer = AnimalSerializer(animal)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         animal = get_object_or_404(Animal.objects.all(), pk=pk)
#         serializer = AnimalSerializer(animal, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         animal = get_object_or_404(Animal.objects.all(), pk=pk)
#         serializer = AnimalSerializer(animal, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         animal = get_object_or_404(Animal.objects.all(), pk=pk)
#         animal.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     @action(detail=True, methods=['get'])
#     def passport(self, request, pk=None):
#         """
#         Получение паспорта животного
#         """
#         animal = get_object_or_404(Animal.objects.all(), pk=pk)
#         passport = get_object_or_404(AnimalPassport.objects.all(), animal=animal)
#         serializer = AnimalPassportSerializer(passport)
#         return Response(serializer.data)

#     @action(detail=True, methods=['get'])
#     def vaccinations(self, request, pk=None):
#         """
#         Получение списка вакцинаций животного
#         """
#         animal = get_object_or_404(Animal.objects.all(), pk=pk)
#         vaccinations = Vaccination.objects.filter(animal=animal)
#         serializer = VaccinationSerializer(vaccinations, many=True)
#         return Response(serializer.data)

#     @action(detail=True, methods=['get'])
#     def treatments(self, request, pk=None):
#         """
#         Получение списка лечений животного
#         """
#         animal = get_object_or_404(Animal.objects.all(), pk=pk)
#         treatments = Treatment.objects.filter(animal=animal)
#         serializer = TreatmentSerializer(treatments, many=True)
#         return Response(serializer.data)


# class AnimalPassportViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet для работы с паспортами животных
#     """
#     def list(self, request):
#         queryset = AnimalPassport.objects.all()
#         serializer = AnimalPassportSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = AnimalPassportSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = AnimalPassport.objects.all()
#         passport = get_object_or_404(queryset, pk=pk)
#         serializer = AnimalPassportSerializer(passport)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         passport = get_object_or_404(AnimalPassport.objects.all(), pk=pk)
#         serializer = AnimalPassportSerializer(passport, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         passport = get_object_or_404(AnimalPassport.objects.all(), pk=pk)
#         serializer = AnimalPassportSerializer(passport, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         passport = get_object_or_404(AnimalPassport.objects.all(), pk=pk)
#         passport.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class VaccinationViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet для работы с вакцинациями
#     """
#     def list(self, request):
#         queryset = Vaccination.objects.all()
#         serializer = VaccinationSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = VaccinationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Vaccination.objects.all()
#         vaccination = get_object_or_404(queryset, pk=pk)
#         serializer = VaccinationSerializer(vaccination)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         vaccination = get_object_or_404(Vaccination.objects.all(), pk=pk)
#         serializer = VaccinationSerializer(vaccination, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         vaccination = get_object_or_404(Vaccination.objects.all(), pk=pk)
#         serializer = VaccinationSerializer(vaccination, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         vaccination = get_object_or_404(Vaccination.objects.all(), pk=pk)
#         vaccination.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class TreatmentViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet для работы с лечениями
#     """
#     def list(self, request):
#         queryset = Treatment.objects.all()
#         serializer = TreatmentSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = TreatmentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def retrieve(self, request, pk=None):
#         queryset = Treatment.objects.all()
#         treatment = get_object_or_404(queryset, pk=pk)
#         serializer = TreatmentSerializer(treatment)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         treatment = get_object_or_404(Treatment.objects.all(), pk=pk)
#         serializer = TreatmentSerializer(treatment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         treatment = get_object_or_404(Treatment.objects.all(), pk=pk)
#         serializer = TreatmentSerializer(treatment, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         treatment = get_object_or_404(Treatment.objects.all(), pk=pk)
#         treatment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)