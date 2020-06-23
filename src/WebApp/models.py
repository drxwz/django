from django.db import models

# Create your models here.

class Client(models.Model):
	client_name = models.CharField(max_length =100)
	client_adress = models.CharField(max_length = 100)
	client_email = models.CharField(max_length = 100)
	client_phone = models.CharField(max_length = 100)

	def __str__(self):
		return self.client_adress
		return self.client_name
		return self.client_email
		return self.client_phone