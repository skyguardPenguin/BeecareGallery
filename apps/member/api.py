from rest_framework.decorators import  action
from .models import memberphoto
from .serializers import memberphotoSerializer
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from django.http import HttpResponse

class memberphotoViewSet(viewsets.ModelViewSet):
    queryset = memberphoto.objects.all()
    permission_classes= [permissions.IsAuthenticated]
    serializer_class = memberphotoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        id = serializer.instance.id

        response = {"id": id}
        return Response(response, status=200)


    @action(detail=True, methods=['get'])
    def get_image(self, request, pk=None):
        obj = self.get_object()
        path = obj.loadImage.path

        with open(path, 'rb') as archivo_imagen:
            imagen_bytes = archivo_imagen.read()

        return HttpResponse(imagen_bytes, content_type='image/jpeg')


