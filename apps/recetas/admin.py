from django.contrib import admin
from .models import Receta

class IndexReceita(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'categoria', 'tiempo_preparacion', 'publicada', 'persona')
    list_display_links = ('id', 'nombre')
    search_fields = ('nombre',)
    list_filter = ('categoria',)
    list_editable = ('publicada',)
    list_per_page = 10

admin.site.register(Receta, IndexReceita)
