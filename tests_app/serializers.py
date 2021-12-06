from rest_framework import serializers

from .models import Puppy

class Puppy_serializers(serializers.ModelSerializer):

    class Meta:
        model = Puppy
        fields = '__all__'
