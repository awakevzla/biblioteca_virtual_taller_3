from rest_framework import serializers
from .models import Usuario

class UsuarioRegistroSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, label='Confirmar contraseña', style={'input_type': 'password'})
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'password2', 'first_name', 'last_name', 'rol', 'ciudad']
        extra_kwargs = {
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
        }
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')
        usuario = Usuario(**validated_data)
        usuario.set_password(password)
        usuario.save()
        return usuario

class UsuarioSerializer(serializers.ModelSerializer):
    prestamos_activos = serializers.SerializerMethodField()
    
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'rol', 'ciudad', 'date_joined', 'prestamos_activos']
        read_only_fields = ['id', 'date_joined']
    
    def get_prestamos_activos(self, obj):
        """Retorna los préstamos activos (no devueltos) del usuario"""
        from prestamos.models import Prestamo
        prestamos = Prestamo.objects.filter(usuario=obj, fecha_devolucion__isnull=True)
        return [{
            'id': prestamo.id,
            'libro_titulo': prestamo.libro.titulo,
            'libro_id': prestamo.libro.id,
            'fecha_prestamo': prestamo.fecha_prestamo,
        } for prestamo in prestamos]
