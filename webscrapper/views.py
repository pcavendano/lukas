from django.shortcuts import render

# Create your views here.

def home(requests):
    return HttpResponse("Home Page")

def scrappe(requests):
    return HttpResponse("Scrapper Page")
