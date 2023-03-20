from rest_framework import serializers
from .models import load

class loadSerializer(serializers.ModelSerializer):
    class Meta:
        model = load
        fields = ('id','loadRoute', 'loadDate', 'loadImage')
        read_only_fields = ('loadRoute','loadDate',)
