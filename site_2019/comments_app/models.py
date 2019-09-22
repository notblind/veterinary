from django.db import models

# Create your models here.

class CommentsModel(models.Model):
	surname = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	message = models.CharField(max_length=3000)
	timedate = models.DateTimeField(auto_now_add=True)
