__author__ = "Lário dos Santos Diniz"

from django.test import TestCase

from model_mommy import mommy
from core.models import Genre, Artist

class ArtistModelTestCase(TestCase):
    """Testing the model Artist"""

    def setUp(self):
        """Initial Test Settings"""
        self.genre = mommy.make(Genre, name='test genre')
        self.artist = mommy.make(Artist, genres=[self.genre])

    def tearDown(self):
        """Final method"""
        self.artist.delete()
        self.genre.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name', 'apleId', 'genres']
        
        for fild in filds:
            self.assertTrue(fild in dir(Artist),
                            'Class Artist does not have the field {}'.format(fild))

    def test_there_is_a_artist(self):
        """test if you are creating a Artist correctly"""
        self.assertTrue(isinstance(self.artist, Artist))
        self.assertEquals(Artist.objects.count(), 1)
        artist = Artist.objects.all()[0]
        self.assertEquals(artist.name, self.artist.name)
        self.assertEquals(artist.apleId, self.artist.apleId)
        self.assertEquals(artist.genres.all()[0].name, 'test genre')

    def test_string_representation(self):
        """tests if the presentation is correct"""
        self.assertEqual(str(self.artist), self.artist.name)
        