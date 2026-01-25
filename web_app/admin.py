from django.contrib import admin
from .models import QuoteRequest


@admin.register(QuoteRequest)
class QuoteRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'company', 'service', 'created_at')
    list_filter = ('company','service', 'created_at')
    search_fields = ('name', 'phone', 'email', 'company')