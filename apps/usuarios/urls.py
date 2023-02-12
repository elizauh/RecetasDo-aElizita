from django.urls import path
from .src.controller import *

urlpatterns = [
    path('login', login, name='usuarios.login'),
    path('logout', logout, name='usuarios.logout'),
    path('registro', create, name='registro'),
    path('recetas', dashboard, name='usuarios.dashboard'),
]
