from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Request Handler 

def sayHello(request):
    return HttpResponse('Hello World')