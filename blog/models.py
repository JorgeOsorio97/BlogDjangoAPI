from django.db import models

# Create your models here.
class Entrada(models.Model):
    """ Model that specifies each post in the blog """
    titulo = models.TextField(max_length=150, null=False)
    fecha_publ = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='media/', null=True)
    texto_intro = models.TextField(max_length=250, null=False)
    texto_completo = models.TextField()


