"""Views file of the project"""
from django.http import response
from django.shortcuts import render, redirect
from appflow.models import Project

def homepage(request):
    """Return the hoempage"""
    return render(request, 'homepage.html', {})

def project(request, pk):
    """Return specific project"""
    try:
        proj = Project.objects.get(id=pk)
        return render(request, 'vplayer.html',{'proj':proj})
    except Exception as exc:
        raise exc