from django.shortcuts import render
from django.http import HttpResponse

# Create your views here

def welcome(request):
    return HttpResponse('Welcome to your Django App!')

def teapot(request):
    return HttpResponse("I'm a teapot", status=418)