from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def projects(request):
    return HttpResponse('This is the projects page!!')


def project(request, pk):
    return HttpResponse("This is project" + " " + str(pk))
