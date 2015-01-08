from django import forms
from agenda.models import Contactos, Grupos, Colores


class ContactoForm(forms.ModelForm):
	class Meta:
	        model = Contactos

class GroupForm(forms.ModelForm):
	class Meta:
		model = Grupos

class ColorForm(forms.ModelForm):
	class Meta:
		model = Colores
