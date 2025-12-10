from .models import Libro
from .serializers import LibroSerializer
from rest_framework import viewsets

class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer