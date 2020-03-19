from django.urls import path
from django.views import generic

from . import views
from . import forms
from .models import *

urlpatterns = [
    path('', views.index_proveedores, name='index_proveedores'),
    path('nuevo/', views.proveedores_view, name='proveedores_view'),
    path("ajax/load-ciudades/",views.load_ciudades, name="ajax_load_ciudades"),
    path('editar/<pk>', views.proveedores_editar, name='proveedores_editar'),

]