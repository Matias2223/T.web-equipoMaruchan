from django.db import models
from django import forms

class usuarios(models.Model):
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length = 100)
    user = models.CharField(max_length = 50)
    contra = models.CharField(max_length = 100)
    rol = models.CharField(max_length = 20, null = True)
    tel = models.CharField(max_length = 10)
    email = models.EmailField(max_length = 100)

    class Meta:
        db_table = "usuarios"

    # Muestra los datos en el administrador de Django
    def __str__(self):
        fila = "Nombre: " + self.nombre + "Usuario: " + self.user + "Contraseña: " + self.contra + "Rol: " + self.rol + "Teléfono: " + self.tel + "Correo: " + self.email
        return fila
    
    # Borrar desde el administrador de Django
    def delete(self, using = None, keep_parents = False):
        super().delete()
