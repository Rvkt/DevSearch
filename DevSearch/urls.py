from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


def projects(request):
    return HttpResponse('This is the projects page!!')


def project(request, pk):
    return HttpResponse("This is project" + " " + str(pk))


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', projects, name="projects"),
    path('project/<str:pk>/', project, name="project"),
]

# path('urlName/', function_Name, name="ReferenceName"),
