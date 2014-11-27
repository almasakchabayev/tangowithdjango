from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<a href="about/">About</a>')

def about(request):
    return HttpResponse('<a href="../">Index</a>')