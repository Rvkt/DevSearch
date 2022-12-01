from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import ProjectForm
from .models import Project


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


@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project-form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project-form.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == "POST":
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'delete-template.html', context)
