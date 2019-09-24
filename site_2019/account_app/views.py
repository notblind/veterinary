from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from veterinary_app.models import doctors
from veterinary_app.models import positions
from .forms import ChangeForm

from django.views import generic
from django.views.generic import View

from django.core.files.storage import FileSystemStorage

# Create your views here.

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'account_app/signup.html'

@login_required
def Personal(request, user=0):
	user = None
	if request.user.is_authenticated:
		user = request.user.id
	try:
		doctor = doctors.objects.get(user=user)
	except:
		doctor = None
	return render(request, 'account_app/personal.html', context={'doctor': doctor})

class Change(View):
	
	@login_required
	def get(self, request):
		form = ChangeForm()
		if request.user.is_authenticated:
			try:
				doctor = doctors.objects.get(user=request.user.id)
			except:
				doctor = None
			if doctor != None:
				initial = {
					'name': request.user.first_name,
					'surname': request.user.last_name,
					'middle': doctor.middle,
					'email': request.user.email,
					'education': doctor.education,
					'interests': doctor.interests,
					'position':  doctor.position,
					'foto':  doctor.foto,
				}
				form = ChangeForm(initial=initial)
			else:
				form = ChangeForm()
		return render(request, 'account_app/change.html', context={'form': form})

	@login_required
	def post(self, request):
		form = ChangeForm(request.POST, request.FILES)
	
		if form.is_valid():
			name = form.cleaned_data['name']
			surname = form.cleaned_data['surname']
			middle = form.cleaned_data['middle']
			email = form.cleaned_data['email']
			education = form.cleaned_data['education']
			interests = form.cleaned_data['interests']
			position = form.cleaned_data['position']
	
			try:
				foto = request.FILES['foto']
			except:
				foto = None


			user_id = request.user.id
			try:
				pos = positions.objects.get(name=position[0])
			except:
				pos = positions.objects.get(name='хирург')
			try:
				doctor_model = doctors.objects.get(user=user_id)
			except:
				doctor_model = None
			user_model = User.objects.get(id=user_id)
			user_model.email = email
			user_model.firt_name = name
			user_model.last_name = surname
			user_model.save()
	
			if doctor_model != None:
				doctor_model.middle = middle
				doctor_model.education = education
				doctor_model.interests = interests
				doctor_model.position = pos
				if foto != None:
					doctor_model.foto = foto
				doctor_model.save()



			return redirect('personal')
		return redirect('main_page')


from django.contrib.auth import logout

@login_required
def LogOut(request):
	logout(request)
	return reverse_lazy(main_page)



