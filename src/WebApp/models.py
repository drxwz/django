from django.db import models

# Create your models here.

class Adress(models.Model):
	client_adress = models.CharField(max_length = 100)
	client_email = models.CharField(max_length = 100)
	client_phone = models.CharField(max_length = 100)

	def __str__(self):
		return self.client_adress