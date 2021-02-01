from django.db import models

# Create your models here.
class FbModel(models.Model):
	name=models.CharField(max_length=30)
	feedback=models.TextField()

	def __str__(self):
		return self.name