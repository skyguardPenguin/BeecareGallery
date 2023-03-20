from rest_framework import serializers
from .models import beephoto
from .models import species
from .models import sightings

class speciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = species
        fields = ('id','specieName')

class sightingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = sightings
        fields = ('id','specie','isBee','isLocal')

class beephotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = beephoto
        fields = ('id','loadRoute', 'loadDate', 'loadImage','sighting')
        read_only_fields = ('loadRoute','loadDate',)







