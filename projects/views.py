from django.shortcuts import render
from django.http import HttpResponse


def projects(request):
    return render(request, 'projects/projects.html')


def project(request, pk):
    return render(request, 'projects/single-project.html')


def createProject(request):
    return render(request, "projects/project-form.html")


def updateProject(request):
    return render(request, "projects/project-form.html")


def deleteProject(request):
    return render(request, 'delete-template.html')
