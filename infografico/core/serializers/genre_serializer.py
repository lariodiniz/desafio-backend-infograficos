__author__ = "Lario dos Santos Diniz"

from rest_framework import serializers

from core.models import Genre

class GenreSerializer(serializers.ModelSerializer):
    """Genre Serializer class"""
    
    class Meta:
        model = Genre
        fields = ['name']
