from django.urls import path
from .views import *

urlpatterns = [
	path('', MainPage, name='main_page'),
	path('doctors/<str:slug>/', Doctors, name='doctors'),
	path('doctor/<int:id>/', DoctorDetail, name='doctor_detail'),
	path('services/', Services, name='services'),
]