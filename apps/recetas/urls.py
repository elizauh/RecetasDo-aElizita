from django.urls import path
from .src.controller import *
# from .src.controllers.ReceitaController import *

urlpatterns = [
    path('', index, name='recetas.index'),
    path('criar', create, name='recetas.create'),
    path('<int:receta_id>', show, name='recetas.show'),
    path('editar/<int:receta_id>', edit, name='recetas.edit'),
    path('deletar/<int:receta_id>', destroy, name='recetas.destroy'),
    # rota para o campo de busca
]
