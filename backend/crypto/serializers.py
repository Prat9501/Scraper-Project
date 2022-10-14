from dataclasses import field
from rest_framework import serializers
from .models import CurrencyData


class CurrencyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyData
        fields = '__all__'