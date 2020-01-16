# coding: utf-8
__author__ = "Lário dos Santos Diniz"

import json

from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.urls import reverse

from model_mommy import mommy

from core.models import Artist, Genre


class ArtistViewTestCase(APITestCase):
    """test user view"""
    def setUp(self):
        """Initial Test Settings"""
        self.genre = mommy.make(Genre, name='test genre')
        self.artist = mommy.make(Artist, genres=[self.genre])
        self.url = reverse('core:artist_list')        
        self.client = APIClient()        

    def tearDown(self):
        self.genre.delete()
        self.artist.delete()

    def test_artist_list_view_get(self):        
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, 200, 
                          'a get request for url "{}" is not returning status code 200'.format(self.url))        
        

    def test_artist_list_view_object(self):        
        response = self.client.get(self.url)        
        self.assertEqual(len(response.data), 1)        
        self.assertEqual(json.loads(response.content), json.loads())        
