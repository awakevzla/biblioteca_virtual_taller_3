from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    publicado_en = models.DateField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo + " by " + self.autor + " (ISBN: " + self.isbn + ")"
    
    class Meta:
        ordering = ['titulo']
