from django import forms

class CommentsForm(forms.Form):
	surname = forms.CharField(label='Ваша фамилия', max_length=128, required=True)
	name = forms.CharField(label='Ваше имя', max_length=128, required=True)
	message = forms.CharField(label='Ваш отзыв', max_length=300, required=True, widget=forms.Textarea)

	surname.widget.attrs.update({'class':'form-control', 'placeholder':'Фамилия'})
	name.widget.attrs.update({'class':'form-control', 'placeholder':'Имя'})
	message.widget.attrs.update({'class':'form-control', 'placeholder':'Сообщение', 'rows':6})

