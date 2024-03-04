from django.shortcuts import render
# Create your views here.

smartphones_data = [
    { 'id':1}
]

def home(requests):
    context = {'smartphones_data':smartphones_data}
    return render(requests, 'webscrapper/home.html', context)

def scrappe(requests):
    return render(requests, 'webscrapper/scrapper.html')
