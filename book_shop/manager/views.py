from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# Test view hello()
def hello(request, name):
    return HttpResponse(f"Hello Django from {name}!")
