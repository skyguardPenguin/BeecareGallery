from .models import load
from .serializers import loadSerializer
from rest_framework import viewsets, permissions

class loadViewSet(viewsets.ModelViewSet):
    queryset = load.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = loadSerializer