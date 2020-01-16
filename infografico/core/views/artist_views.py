from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from core.models import Artist
from core.serializers import ArtistSerializer

class ArtistList(APIView):
    """
    List all artist.
    """
    def get(self, request, format=None):
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        raise Http404("forbidden post type requests")