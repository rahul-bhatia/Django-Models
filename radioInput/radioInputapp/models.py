from django.db import models

# Create your models here.
class RaInput(models.Model):
	name=models.CharField(max_length=30)
	options=models.CharField(max_length=10)

	def __str__(self):
		return self.name