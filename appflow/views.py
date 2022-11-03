from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializerfile import SnippetSerializer
from .models import Project
# Create your views here.
@api_view(['GET'])
def projects(request):
    """Serializer used to return projects data"""
    try:
        projs = Project.objects.all().order_by('-created_on')
        serializer = SnippetSerializer(projs, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Exception as exc:
        raise exc