from django.contrib import admin

# Register your models here.
from .models import Oficio


@admin.register(Oficio)
class OficioAdmin(admin.ModelAdmin):
    list_display = ('cabecalho', 'paragrafo_um', 'paragrafo_dois', 'rodape', 'endereco', 'telefone')