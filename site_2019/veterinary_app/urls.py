from django.urls import path
from .views import *

urlpatterns = [
	path('', MainPage, name='main_page'),
	path('doctors/<str:slug>/', Doctors, name='doctors'),
	path('doctor/<int:id>/', DoctorDetail, name='doctor_detail'),
	path('services/', Services, name='services'),
	path('orders/', Orders, name='order'),
	path('neworder/', NewOrder.as_view(), name='new_order'),
	path('deleteorder/<str:id>/', DeleteOrder, name='delete_order'),
	path('changeorder/<str:id>/', ChangeOrder.as_view(), name='change_order'),
]