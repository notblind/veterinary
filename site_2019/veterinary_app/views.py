from django.shortcuts import render
from django.shortcuts import redirect

from .models import *

from django.contrib.auth.models import User

from django.core.paginator import Paginator

from django.views.generic import View
# Create your views here.

def MainPage(request):
	if request.user.is_authenticated:
		try:
			doctor = doctors.objects.get(user=request.user.id)
		except:
			doctor = None
	return render(request, 'veterinary_app/mainpage.html', context={'doctor': doctor})

def Doctors(request, slug='all'):

	dictionary = ('А','Б','В','Г','Д','Е','Ж','З','И','К','Л','М','Н','О','П','Р','С','Т','Ф','Х','Ч','Ш')
	letter = request.GET.get('letter', '')
	

	if slug=='all':
		#doctor_list = doctors.objects.all().filter(surname__startswith=letter)
		doctor_list = doctors.objects.all()
	else: 
		position = positions.objects.get(slug=slug)
		#doctor_list = doctors.objects.filter(position=position, surname__startswith=letter)
		doctor_list = doctors.objects.filter(position=position)
	position_list = positions.objects.all()

	paginator = Paginator(doctor_list, 9)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = '?page={}'.format(page.previous_page_number())
	else:
		prev_url = ''

	if page.has_next():
		next_url = '?page={}'.format(page.next_page_number())
	else:
		next_url = ''

	context = {
		'doc': page,
		'position': position_list,
		'number': slug,
		'prev_url':prev_url,
		'next_url':next_url,
		'is_paginated':is_paginated,
		'dictionary': dictionary,
		'letter': letter,
	}
	return render(request, 'veterinary_app/doctors.html', context=context)

def DoctorDetail(request, id):
	doctor = doctors.objects.get(id=id)
	return render(request, 'veterinary_app/doctor.html', context={'doc': doctor})

def Services(request):
	service_list = services.objects.all()
	position_list = positions.objects.all()
	context = {
		'services': service_list,
		'positions': position_list,
	}
	return render(request, 'veterinary_app/services.html', context=context)


from .forms import HealForm

class NewOrder(View):

	def get(self, request):
		form = HealForm()
		return render(request, 'veterinary_app/new_order.html', context={'form': form})

	def post(self, request):
		form = HealForm(request.POST)
		if form.is_valid():
			animal = form.cleaned_data['animal']
			owner_surname = form.cleaned_data['owner_surname']
			owner_name = form.cleaned_data['owner_name']
			services = form.cleaned_data['services']
			status = form.cleaned_data['status']
			try:
				doctor = doctors.objects.get(user=request.user.id)
			except:
				doctor = None
			new_order = heal(doctor=doctor, animal=animal, owner_surname=owner_surname, owner_name=owner_name, status=status)
			new_order.save()
			new_order.services.set(services)
		return redirect('order')


def Orders(request):
	heals = None
	if request.user.is_authenticated:
		try:
			doctor = doctors.objects.get(user=request.user.id)
		except:
			doctor = None
	if doctor != None:
			heals = heal.objects.all().filter(doctor=doctor).order_by('-datetime')
	serv = services.objects.all()
	return render(request, 'veterinary_app/orders.html', context={'heals': heals, 'serv': serv})

def DeleteOrder(request, id=None):
	try:
		h = heal.objects.get(id=id)
	except:
		h = None
	h.delete()
	return redirect('order')

class ChangeOrder(View):

	def get(self, request, id=None):
		try:
			h = heal.objects.get(id=id)
		except:
			h = None
		if h != None:
			initial = {
				'animal': h.animal,
				'owner_surname': h.owner_surname,
				'owner_name': h.owner_name,
				'services': h.services.all,
				'status': h.status,
			}
			form = HealForm(initial=initial)
		else:
			form = HealForm()
		return render(request, 'veterinary_app/change_order.html', context={'form': form})

	def post(self, request, id=None):
		form = HealForm(request.POST)
		if form.is_valid():
			animal = form.cleaned_data['animal']
			owner_surname = form.cleaned_data['owner_surname']
			owner_name = form.cleaned_data['owner_name']
			services = form.cleaned_data['services']
			status = form.cleaned_data['status']
			try:
				h = heal.objects.get(id=id)
			except:
				h = None
			if h != None:
				h.animal=animal
				h.owner_surname=owner_surname
				h.owner_name=owner_name
				h.status=status
				h.services.clear()
				h.services.set(services)
				h.save()

		return redirect('order')