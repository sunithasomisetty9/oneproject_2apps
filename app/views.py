from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def first(request):
    return HttpResponse("Hello Good Afternoon")

def second(request):
    return HttpResponse("This is my second view")

def login(request):
    return render(request,'login.html')

def regform(request):
    return render(request,'regform.html')