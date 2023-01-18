from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def sreenu(request,name):
    return HttpResponse(f'Welcome to jspyders {name}')
