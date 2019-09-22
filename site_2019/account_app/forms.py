from django import forms
from django.contrib.auth.models import User
from veterinary_app.models import positions

from django.contrib.auth.forms import AuthenticationForm

class ChangeForm(forms.Form):
	name = forms.CharField(label='Имя', max_length=30, required=False)
	surname = forms.CharField(label='Фамилия', max_length=150, required=False)
	middle = forms.CharField(label='Отчество', max_length=128, required=False)
	email = forms.EmailField(label='Email', required=False)
	education = forms.CharField(label='Образование', max_length=1500, required=False)
	interests = forms.CharField(label='Профессиональные интересы', max_length=1500, required=False)
	position = forms.ModelChoiceField(label='Специализация', queryset=positions.objects.all())
	foto = forms.ImageField(label='Фото', required=False)
