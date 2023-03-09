from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def vinod(request):
    return HttpResponse('<b><h1>Vinod is one and one only son of Sekhar</b></h1>')