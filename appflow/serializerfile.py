"""Serializer file"""
from rest_framework import serializers
from .models import Project

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id','project','created_on','files']
