from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Documento


class DocumentoForm(forms.ModelForm):
    contenido = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Documento
        fields = ["titulo", "contenido"]
