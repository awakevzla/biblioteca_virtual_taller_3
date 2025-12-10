from django.db import models

class Prestamo(models.Model):
    libro = models.ForeignKey('libros.Libro', on_delete=models.CASCADE)
    usuario = models.ForeignKey('usuarios.Usuario', on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(auto_now_add=True)
    fecha_devolucion = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.libro.titulo} prestado a {self.usuario} el {self.fecha_prestamo}"