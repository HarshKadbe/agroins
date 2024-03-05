from rest_framework import serializers
from projects.models import PredictDisease, PredictedData


class PredictDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictedData
        fields = ['nitrogen', 'phosphorus', 'pottasium', 'temperature', 'humidity', 'ph', 'rainfall']
        
