from rest_framework import serializers
from .models import beephoto


class beephotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = beephoto
        fields = ('id', 'loadDate', 'loadImage')
        read_only_fields = ('loadDate',)







