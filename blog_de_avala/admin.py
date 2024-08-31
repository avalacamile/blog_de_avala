from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Pessoa)
class EuAdmin (admin.ModelAdmin):
    list_display=('nome','idade', 'email','foto')

@admin.register(Sobre)
class SobreAdmin (admin.ModelAdmin):
    list_display=('escola','curso', 'ano')

# Register your models here.
