from django.contrib import admin
from .models import QuoteRequest
from .models import Proyecto


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'company', 'service', 'created_at')
    list_filter = ('company','service', 'created_at')
    search_fields = ('name', 'phone', 'email', 'company')

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'tipo', 'fecha_publicacion', 'destacado')
    list_filter = ('tipo', 'destacado', 'fecha_publicacion')
    search_fields = ('titulo', 'descripcion_corta')