from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


# CRUD
def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    tag = projectObj.tags.all()
    context = {'project': projectObj, 'tags': tag}
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, "projects/project-form.html", context)


def updateProject(request):
    return render(request, "projects/project-form.html")


def deleteProject(request):
    return render(request, 'delete-template.html')
