from django.shortcuts import render
# Create your views here.

def home(requests):
    return render(requests, 'base.html', {'name': 'Lukas'})

def scrappe(requests):
    return render(requests, 'scrappe.html', {'name': 'Lukas'})
