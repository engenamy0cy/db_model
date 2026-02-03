from rest_framework import serializers
from .models import Car, Company, Color

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    color_name = serializers.CharField(source = 'color.name', read_only = True)
    company_name = serializers.CharField(source = 'company.name', read_only = True)
    class Meta:
        model = Car
        fields = '__all__' #__all__