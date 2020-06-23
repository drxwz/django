from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
	return render(request, 'WebApp/dashboard.html')


def customer(request):
	return render(request, 'WebApp/customer.html')


def products(request):
	return render(request, 'WebApp/products.html')