from rest_framework import serializers
from datetime import datetime
from rest_framework.validators import UniqueTogetherValidator

from productoapi.models import Producto
def validar_precio(value):
    if value % 10 !=0:
        raise serializers.ValidationError("Debe ser un multiplo de 10")

class ProductoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    descripcion=serializers.CharField()
    imagen=serializers.FileField()

    def create(self,validated_data):
        return Producto(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.descripcion = validated_data.get('descripcion',instance.descripcion)
        return instance
    def validate_name(self,value):
        if 'prohibido' in value.lower():
            raise serializers.ValidationError("prohibido no debe estar en el nombre")
        return value
    def validate(self,data):
        if 'prohibido' in data['descripcion']:
            raise serializers.ValidationError("prohibido no debe estar en la descripcion")
        return data
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Producto.objects.all(),
                fields=['precio']
            )
        ]

class ProductoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['name','descripcion'] 