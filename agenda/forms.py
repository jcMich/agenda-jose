from django import forms
from agenda.models import Contactos


class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contactos
