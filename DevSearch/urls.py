from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def projects(request):
    return HttpResponse('This is the projects page!!')


def project(request):
    return HttpResponse("This is single project page!!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('project/', project, name="project"),
    path('projects/', projects, name="projects"),
]

# path('urlName/', function_Name, name="ReferenceName"),
