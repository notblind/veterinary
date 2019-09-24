from django import forms
from django.contrib.auth.models import User
from veterinary_app.models import positions
from .models import *

from django.contrib.auth.forms import AuthenticationForm

class HealForm(forms.Form):

	services = forms.ModelMultipleChoiceField(queryset=None, label='Предоставляемые услуги', required=True)

	def __init__(self, *args, **kwargs):
		position = kwargs.pop('position', None)
		super(HealForm, self).__init__(*args, **kwargs)
		
		self.fields['services'].queryset = services.objects.filter(position=position)
	
	animal = forms.ModelChoiceField(label='Животное', queryset=animals.objects.all(), required=True)
	owner_surname = forms.CharField(label='Фамилия владельца', max_length=128, required=True)
	owner_name = forms.CharField(label='Имя владельца', max_length=128, required=True)
	status = forms.ModelChoiceField(label='Статус', queryset=status.objects.all(), required=True)
