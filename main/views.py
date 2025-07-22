from django.shortcuts import render
from django.http import HttpResponse # required lib to send httpresponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World!")
