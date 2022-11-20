from http.client import HTTPResponse
import re
from unittest import result
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Parvez'})

# def add(request):
#     val1 = int(request.GET['num1'])
#     val2 = int(request.GET['num2'])
#     res = val1 + val2

#     return render(request, "result.html", {'result':res })

def subtract(request):
    value1 = int(request.POST['number1'])
    value2 = int(request.POST['number2'])
    res = value1 - value2

    return render(request, "result.html", {'result':res})
    