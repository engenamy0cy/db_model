from rest_framework import serializers
from .models import RAM,CPU,GPU,PC, Manufacturer

class RAMSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAM
        fields = '__all__'

class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = '__all__'

class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = '__all__'
        
class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = '__all__'

class PCSerializer(serializers.ModelSerializer):
    cpu_name = serializers.CharField(source = 'cpu.name', read_only = True)
    gpu_name = serializers.CharField(source = 'gpu.name', read_only = True)
    ram_name = serializers.CharField(source = 'ram.name', read_only = True)
    class Meta:
        model = PC
        fields = '__all__'