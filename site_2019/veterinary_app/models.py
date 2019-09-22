from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class positions(models.Model):
	name = models.CharField(max_length=256)
	slug = models.SlugField(max_length=64, unique=True)

	def __str__(self):
		return self.name

class services(models.Model):
	name = models.CharField(max_length=128)
	cost = models.CharField(max_length=128)
	position = models.ForeignKey(positions, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class doctors(models.Model):
	middle = models.CharField(max_length=128)
	education = models.CharField(max_length=1500)
	interests = models.CharField(max_length=1500)
	position = models.ForeignKey(positions, on_delete=models.CASCADE)
	foto = models.ImageField(null=True, blank=True)
	user = models.OneToOneField(User, on_delete = models.CASCADE, blank=True)

class animals(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class status(models.Model):
	name = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class heal(models.Model):
	doctor = models.ForeignKey(doctors, on_delete=models.CASCADE)
	animal = models.ForeignKey(animals, on_delete=models.CASCADE)
	owner_surname = models.CharField(max_length=128)
	owner_name = models.CharField(max_length=128)
	services = models.ManyToManyField(services)
	status = models.ForeignKey(status, on_delete=models.CASCADE)
	datetime = models.DateTimeField(auto_now_add=True)


