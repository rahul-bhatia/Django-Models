from django.db import models

# Create your models here.

class EnModel(models.Model):
	name=models.CharField(max_length=20)
	email=models.EmailField(max_length=20)
	phone=models.CharField(max_length=10)

	def __str__(self):
		return self.name

