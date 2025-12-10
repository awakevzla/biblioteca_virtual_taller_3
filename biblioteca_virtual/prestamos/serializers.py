from rest_framework import serializers
from .models import Prestamo

class PrestamoSerializer(serializers.ModelSerializer):
    libro_titulo = serializers.CharField(source='libro.titulo', read_only=True)
    usuario_nombre = serializers.CharField(source='usuario.username', read_only=True)
    usuario_rol = serializers.CharField(source='usuario.rol', read_only=True)
    
    class Meta:
        model = Prestamo
        fields = ['id', 'libro', 'libro_titulo', 'usuario', 'usuario_nombre', 'usuario_rol', 'fecha_prestamo', 'fecha_devolucion']
        read_only_fields = ['usuario']
    
    def validate_libro(self, value):
        """Valida que el libro esté disponible antes de crear un préstamo"""
        if not value.disponible:
            raise serializers.ValidationError(
                f"El libro '{value.titulo}' no está disponible para préstamo."
            )
        return value
    
    def create(self, validated_data):
        """Al crear un préstamo, marca el libro como no disponible"""
        libro = validated_data['libro']
        libro.disponible = False
        libro.save()
        return super().create(validated_data)