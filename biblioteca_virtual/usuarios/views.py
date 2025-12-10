from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Usuario
from .serializers import UsuarioRegistroSerializer, UsuarioSerializer

class RegistroUsuarioView(generics.CreateAPIView):
    """
    Endpoint para registrar nuevos usuarios.
    POST /api/usuarios/registro/
    """
    queryset = Usuario.objects.all()
    serializer_class = UsuarioRegistroSerializer
    permission_classes = [permissions.AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()
        
        # Crear token para el nuevo usuario
        token, created = Token.objects.get_or_create(user=usuario)
        
        # Serializar los datos del usuario para la respuesta
        usuario_serializer = UsuarioSerializer(usuario)
        
        return Response({
            'usuario': usuario_serializer.data,
            'token': token.key,
            'message': 'Usuario registrado exitosamente.'
        }, status=status.HTTP_201_CREATED)

class PerfilUsuarioView(generics.RetrieveUpdateAPIView):
    """
    Endpoint para ver y actualizar el perfil del usuario autenticado.
    GET/PUT/PATCH /api/usuarios/perfil/
    """
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user
