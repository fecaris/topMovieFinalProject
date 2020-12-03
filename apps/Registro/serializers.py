from rest_framework import serializers
from .models import Actor

class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'