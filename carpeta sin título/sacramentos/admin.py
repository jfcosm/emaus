from django.contrib import admin
from .models import Sacramento


@admin.register(Sacramento)
class SacramentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'tipo', 'fecha')
    list_filter = ('tipo',)
