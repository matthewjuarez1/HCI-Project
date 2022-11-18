from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return render(response, "main/base.html", {})

def home(response):
    response.user
    return render(response, 'main/home.html',{})

def create(response):
    return render(response, 'main/create.html',{})

def write(response, type):
    return render(response, 'main/write.html', {"type":type})
