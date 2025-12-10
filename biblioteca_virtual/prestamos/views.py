from .models import Prestamo
from .serializers import PrestamoSerializer
from .permissions import IsAdminOrSuperuser
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
    permission_classes = [IsAuthenticated]
    
    class Meta:
        ordering = ['fecha_prestamo']
    
    def perform_create(self, serializer):
        """Asigna automáticamente el usuario autenticado al préstamo"""
        serializer.save(usuario=self.request.user)
    
    @action(detail=True, methods=['post'])
    def devolver(self, request, pk=None):
        prestamo = self.get_object()
        
        
        
        # Verificar que el préstamo pertenece al usuario loggeado (excepto admin y superuser)
        if not IsAdminOrSuperuser.has_permission(self, request, self):
            if prestamo.usuario != request.user:
                return Response(
                    {'error': 'No tienes permiso para devolver este préstamo. Solo puedes devolver tus propios libros.'},
                    status=status.HTTP_403_FORBIDDEN
                )
        
        # Verificar si ya fue devuelto
        if prestamo.fecha_devolucion:
            return Response(
                {'error': 'Este libro ya fue devuelto anteriormente.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Marcar el libro como disponible
        libro = prestamo.libro
        libro.disponible = True
        libro.save()
        
        # Registrar la fecha de devolución
        prestamo.fecha_devolucion = timezone.now().date()
        prestamo.save()
        
        serializer = self.get_serializer(prestamo)
        return Response(
            {
                'message': f'Libro "{libro.titulo}" devuelto exitosamente.',
                'prestamo': serializer.data
            },
            status=status.HTTP_200_OK
        )