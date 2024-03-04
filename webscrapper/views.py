from django.shortcuts import render
from .model import Devices
# Create your views here.

smartphones_data = [
    { 'id':1, 'name':'Samsung Galaxy S21', 'price': 800, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':2, 'name':'Samsung Galaxy S20', 'price': 700, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':3, 'name':'Samsung Galaxy S10', 'price': 600, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':4, 'name':'Samsung Galaxy S9', 'price': 500, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':5, 'name':'Samsung Galaxy S8', 'price': 400, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':6, 'name':'Samsung Galaxy S7', 'price': 300, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':7, 'name':'Samsung Galaxy S6', 'price': 200, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':8, 'name':'Samsung Galaxy S5', 'price': 100, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':9, 'name':'Samsung Galaxy S4', 'price': 50, 'image': 'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':10, 'name':'Samsung Galaxy S3', 'price': 25, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    { 'id':11, 'name':'Samsung Galaxy S2', 'price': 10, 'image':'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    {'id':12, 'name':'Samsung Galaxy S1', 'price': 5, 'image':  'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    {'id':13, 'name':'Apple iPhone 12', 'price': 800, 'image':  'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    {'id':15, 'name':'Apple iPhone 10', 'price': 600, 'image':  'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},
    {'id':14, 'name':'Apple iPhone 11', 'price': 700, 'image':  'https://www.gizmochina.com/wp-content/uploads/2020/12/1-14-300x300.jpg'},

]


def home(requests):
    context = {'smartphones_data':smartphones_data}
    return render(requests, 'webscrapper/home.html', context)

def scrappe(requests):
    return render(requests, 'webscrapper/scrapper.html')

def device(requests, pk):
    device = None
    for i in smartphones_data:
        if i['id'] == int(pk):
            device = i
    context = {'smartphone':smartphones_data[int(pk)-1]}
    return render(requests, 'webscrapper/device.html', context)