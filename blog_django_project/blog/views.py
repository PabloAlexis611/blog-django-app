from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/home.html')

def about(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog/about.html')
