from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return render(request,'index.html')

def vision(request):
    return render(request,'vision.html')

def contact(request):
    return render(request,'contact.html')

def pintu(request):
    return render(request,'pintu.html')