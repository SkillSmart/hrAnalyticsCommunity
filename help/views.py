from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.
def index(request):
    return HttpResponse("The index for the HELP Section")