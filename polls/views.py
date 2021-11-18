from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is http response from the polls app")

def about(request):
    return HttpResponse("This is about page from user_2")