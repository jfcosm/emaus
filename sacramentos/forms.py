# sacramentos/forms.py

from django import forms
from .models import Bautizo

class BautizoForm(forms.ModelForm):
    class Meta:
        model = Bautizo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            classes = field.widget.attrs.get('class', '')
            field.widget.attrs['class'] = f'{classes} form-control'.strip()

        # Aplicar input tipo fecha para campo fecha
        self.fields['fecha'].widget.input_type = 'date'





from django import forms
from .models import Matrimonio



class MatrimonioForm(forms.ModelForm):
    class Meta:
        model = Matrimonio
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

        # Forzar el campo de fecha para usar input type="date"
        if 'fecha' in self.fields:
            self.fields['fecha'].widget.input_type = 'date'
