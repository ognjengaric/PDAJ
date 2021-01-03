from .models import Calculation, Info
from rest_framework import serializers


class InfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Info
        fields = ['n', 'm', 'points']


class CalculationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calculation
        fields = ['result', 'time_in_s', 'max_memory_in_MB']
