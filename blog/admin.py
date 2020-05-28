# Django
from django.contrib import admin

# Models
from blog.models import Entrada
# Register your models here.

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'titulo',
        'fecha_publ',
        'texto_intro'
    )