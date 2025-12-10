from django.contrib import admin
from .models import Libro

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'isbn', 'publicado_en')
    list_filter = ('autor', 'publicado_en')
    search_fields = ('titulo', 'autor', 'isbn')
    ordering = ('titulo',)