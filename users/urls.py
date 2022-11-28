from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('profile/<str:pk>/', views.userProfile, name="user-profile"),
    # CRUD
    # path('create-project/', views.createProject, name="create-project"),
    # path('update-project/<str:pk>/', views.updateProject, name="update-project"),
    # path('delete-project/<str:pk>/', views.deleteProject, name="delete-project"),
]
