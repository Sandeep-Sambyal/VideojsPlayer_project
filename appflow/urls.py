from django.urls import path
from . import views

urlpatterns = [
    path('get-projects/', views.projects, name='projects'),
]