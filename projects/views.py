from django.shortcuts import render
from django.http import HttpResponse


projectsList = [
    {
        'id': '1',
        'title': 'E-commerce Website',
        'description': 'Fully functional e-commerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    context = {'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    return render(request, 'projects/single-project.html')


def createProject(request):
    return render(request, "projects/project-form.html")


def updateProject(request):
    return render(request, "projects/project-form.html")


def deleteProject(request):
    return render(request, 'delete-template.html')
