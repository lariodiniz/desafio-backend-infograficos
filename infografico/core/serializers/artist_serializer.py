__author__ = "Lario dos Santos Diniz"

from rest_framework import serializers

from core.models import Artist
from core.serializers import GenreSerializer

class ArtistSerializer(serializers.ModelSerializer):
    """Artist Serializer class"""
    
    class Meta:
        model = Artist
        fields = ['name', 'apleId', 'genres']

    genres = GenreSerializer(many=True)