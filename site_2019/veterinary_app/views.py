from django.shortcuts import render

from .models import doctors
from .models import positions
from .models import services

from django.contrib.auth.models import User

from django.core.paginator import Paginator
# Create your views here.

def MainPage(request):
	return render(request, 'veterinary_app/mainpage.html')

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
