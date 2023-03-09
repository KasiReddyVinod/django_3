from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sekhar(request):
    return HttpResponse('Sekhar is dad of vinod')
def pullamma(request):
    return HttpResponse('Pullamma is mom of vinod')

