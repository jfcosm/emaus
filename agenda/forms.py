from django import forms
from .models import EventoParroquial

class EventoParroquialForm(forms.ModelForm):
    class Meta:
        model = EventoParroquial
        fields = ['titulo', 'descripcion', 'fecha', 'hora', 'lugar']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for campo in self.fields.values():
            campo.widget.attrs.update({'class': 'form-control'})
