from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def projects(request):
    # return HttpResponse('This is the projects page!!')
    return render(request, 'projects/projects.html')


def project(request, pk):
    # return HttpResponse("This is project" + " " + str(pk))
    return render(request, 'projects/single-project.html')
