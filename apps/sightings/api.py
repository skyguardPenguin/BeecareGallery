from .models import beephoto,species,sightings
from .serializers import beephotoSerializer, speciesSerializer, sightingsSerializer


from rest_framework import viewsets, permissions

class speciesViewSet(viewsets.ModelViewSet):
    queryset = species.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = speciesSerializer

class sightingsViewSet(viewsets.ModelViewSet):
    queryset = sightings.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = sightingsSerializer

class beephotoViewSet(viewsets.ModelViewSet):
    queryset = beephoto.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = beephotoSerializer

