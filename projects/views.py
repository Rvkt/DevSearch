from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projects:
        if i['id'] == pk:
            projectObj = i
    context = {'project': projectObj}
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    return render(request, "projects/project-form.html")


def updateProject(request):
    return render(request, "projects/project-form.html")


def deleteProject(request):
    return render(request, 'delete-template.html')
