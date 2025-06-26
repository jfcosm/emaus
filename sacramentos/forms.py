from django import forms
from .models import Sacramento


class SacramentoForm(forms.ModelForm):
    class Meta:
        model = Sacramento
        fields = ['tipo', 'nombre', 'apellidos', 'fecha', 'observaciones']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'observaciones': forms.Textarea(attrs={'rows': 4}),
        }
