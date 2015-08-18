from django.http import HttpResponse
from django.shortcuts import render

def menu(request):  
    pizzas = Pizza.objects.all()
    result = ''
    for pizza in pizzas:
        result += pizza.name
        result += '<br>'
    return HttpResponse('Hello world') 
