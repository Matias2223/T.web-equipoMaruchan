from django.urls import path
from . import views

# El usuario accede a las vistas

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('index', views.index, name='index'),
    path('sesion', views.sesion, name='sesion'),
    path('registro', views.registro, name='registro'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('editar/<int:id>', views.editar, name='editar'),
    path('insertUser/', views.insertUser, name='insertUser'),
    path('updateUser/', views.updateUser, name='updateUser'),
]