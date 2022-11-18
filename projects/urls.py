from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.projects, name="projects"),
    path('project/<str:pk>/', views.project, name="project"),
    # CRUD
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/', views.updateProject, name="update-project"),
    path('delete-project/', views.deleteProject, name="delete-project"),
]
