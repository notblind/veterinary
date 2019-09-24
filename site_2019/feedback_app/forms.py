from django import forms

class FeedbackForm(forms.Form):
	name = forms.CharField(label='Ваше имя', max_length = 64, required=True)
	email = forms.EmailField(label='Ваша почта', max_length = 128, required=True)
	message = forms.CharField(label='Ваше сообщение', max_length = 3000, widget = forms.Textarea, required=True)

	name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Имя'})
	email.widget.attrs.update({'class': 'form-control', 'placeholder': 'Почта'})
	message.widget.attrs.update({'class':'form-control', 'placeholder': 'Сообщение','rows': '5'})