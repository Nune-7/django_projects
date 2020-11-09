from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	return HttpResponse("Hello Django world!")	
def last_name(request):
	return HttpResponse("I'm Nune Mkrtchyan")
def date_time(request):
	return HttpResponse("It's 10th november 2020")
def task(request):
	a = dict()
	for i in range(1,16):
		a[i] = i**2
	return HttpResponse(a)	
def start(request):
	b = input("Are you ready to start the program?\n a) yes\n b) no\n\t")
	if b == "yes":
		return HttpResponse(b)
	else:
		 break
	