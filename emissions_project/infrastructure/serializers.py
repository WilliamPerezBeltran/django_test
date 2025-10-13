from rest_framework import serializers
from .models import EmissionModel

class EmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmissionModel
        fields = '__all__'
