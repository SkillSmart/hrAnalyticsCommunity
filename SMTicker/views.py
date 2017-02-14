from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def index(request):
    return HttpResponse("Display Social Media Livestream information on People Analytics here.")
