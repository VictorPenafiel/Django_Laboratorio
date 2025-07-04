# C:\Users\victor\Desktop\Repositorios\Django_Laboratorio\config\laboratorio\urls.py
from django.urls import path
from . import views # Importación relativa de las vistas de la misma aplicación 'laboratorio'

urlpatterns = [
    # path('admin/', views.admin, name='admin'), 
    path('insertar/', views.insertar_lab, name='insertar'), 
    path('mostrar/', views.mostrar_lab, name='mostrar'), 
    path('editar/', views.editar_lab, name='editar'), 
    path('eliminar/', views.eliminar_lab, name='eliminar'), 
]