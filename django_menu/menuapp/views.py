from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from menuapp.models import MenuNode


def index(request):
    return render(request, 'menuapp/index.html')

