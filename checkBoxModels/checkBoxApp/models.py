from django.db import models

# Create your models here.
class MaModel(models.Model):
	name=models.CharField(max_length=20)
	notes=models.BooleanField(default=False)
	software=models.BooleanField(default=False)
	certi=models.BooleanField(default=False)

	def __str__(self):
		return self.name