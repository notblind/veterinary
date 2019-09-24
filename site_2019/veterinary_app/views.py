from django.shortcuts import render
from django.shortcuts import redirect

from .models import *

from django.contrib.auth.models import User

from django.core.paginator import Paginator

from django.views.generic import View

from django.contrib.auth.decorators import login_required
# Create your views here.

def MainPage(request):
	return render(request, 'veterinary_app/mainpage.html')

def Doctors(request, slug='all'):

	dictionary = ('А','Б','В','Г','Д','Е','Ж','З','И','К','Л','М','Н','О','П','Р','С','Т','Ф','Х','Ч','Ш')
	letter = request.GET.get('letter', '')
	

	if slug=='all':
		doctor_list = doctors.objects.all().filter(user__last_name__startswith=letter)
	else: 
		position = positions.objects.get(slug=slug)
		doctor_list = doctors.objects.filter(position=position, user__last_name__startswith=letter)
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

	@login_required
	def get(self, request):
		doctor = doctors.objects.get(user=request.user.id)
		form = HealForm(position=doctor.position)
		return render(request, 'veterinary_app/new_order.html', context={'form': form})

	@login_required
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

from django.db.models import Q

@login_required
def Orders(request):
	search = ''
	search = request.GET.get('search', '')


	heals = None
	try:
		doctor = doctors.objects.get(user=request.user.id)
	except:
		doctor = None
	if doctor != None:
		heals = heal.objects.all().filter(Q(doctor=doctor) & (Q(animal__name__icontains=search) | Q(owner_surname__icontains=search) | Q(owner_name__icontains=search) | Q(services__name__icontains=search) | Q(status__name__icontains=search))).order_by('-datetime')
	return render(request, 'veterinary_app/orders.html', context={'heals': heals})

@login_required
def DeleteOrder(request, id=None):
	try:
		h = heal.objects.get(id=id)
	except:
		h = None
	h.delete()
	return redirect('order')

class ChangeOrder(View):

	@login_required
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
			doctor = doctors.objects.get(user=request.user.id)
			form = HealForm(position=doctor.position, initial=initial)
		else:
			doctor = doctors.objects.get(user=request.user.id)
			form = HealForm(position=doctor.position)
		return render(request, 'veterinary_app/change_order.html', context={'form': form})

	@login_required
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