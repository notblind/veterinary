from django.shortcuts import render
from django.shortcuts import redirect

from django.views.generic import View

from .forms import FeedbackForm

from django.core.mail import send_mail, BadHeaderError

# Create your views here.

class Feedback(View):

	def get(self, request):
		if request.user.is_authenticated:
			initial = {
				'name': request.user.first_name,
				'email': request.user.email,
			}
			form = FeedbackForm(initial=initial)
		else:
			form = FeedbackForm()
		return render(request, 'feedback/feedback.html', {'form': form })

	def post(self, request):
		form = FeedbackForm(request.POST)
		if form.is_valid():
			message = form.cleaned_data['message']
			name = form.cleaned_data['name']
			try:
				send_mail(name, message, 'not.blind.post@gmail.com', ['denislee98@gmail.com'])
			except BadHeaderError:
				return redirect('feedback')
		return redirect('feedback')

