from django.db import models

# Create your models here.

# 2 Paso para hacer la migracion a la base de datos, creamos nuestros modelos 
class Libro(models.Model):
    # ID auto increment and primary key
    id = models.AutoField(primary_key = True)
    # Title of the book
    titulo = models.CharField(max_length=100, verbose_name='Titulo')
    # Add img optional
    imagen = models.ImageField(upload_to='imagenes/', null= True, blank=True, verbose_name='Imagen')
    # Add descroptions
    descripcion = models.TextField(null=True, verbose_name='Descripcion')  
    
    
    """ Add a descripcion of the books """
    def __str__(self):
        fila = f'Titulo: {self.titulo} descripcion: {self.descripcion}'
        return fila 
    
    """ Borra imagen  """
    
    def delete(self, using=None, keep_parents =False ):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
    
    