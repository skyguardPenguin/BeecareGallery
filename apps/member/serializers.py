from rest_framework import serializers
from .models import memberphoto

class memberphotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = memberphoto
        fields = ('id', 'loadDate', 'loadImage')
        read_only_fields = ('loadDate',)