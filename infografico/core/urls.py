from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core.views import ArtistList

app_name = 'core'

urlpatterns = [
    path('', ArtistList.as_view(), name='artist_list'),  
]

urlpatterns = format_suffix_patterns(urlpatterns)