__author__ = "Lário dos Santos Diniz"

from django.test import TestCase

from model_mommy import mommy
from core.models import Genre, Artist, Album, Music

class MusicModelTestCase(TestCase):
    """Testing the model Music"""

    def setUp(self):
        """Initial Test Settings"""
        self.genre = mommy.make(Genre, name='test genre')
        self.artist = mommy.make(Artist, name='test artist', genres=[self.genre])
        self.album = mommy.make(Album, name='test album', genres=[self.genre], artists=[self.artist])
        self.music = mommy.make(Music, price=1.5, genres=[self.genre], artists=[self.artist])

    def tearDown(self):
        """Final method"""
        self.artist.delete()
        self.genre.delete()
        self.album.delete()
        self.music.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name', 'collectionName', 'apleId','genres','artists', 'price', 'explicitness', 'discNumber', 'trackTimeMillis']
        
        for fild in filds:
            self.assertTrue(fild in dir(Music),
                            'Class Music does not have the field {}'.format(fild))

    def test_there_is_a_music(self):
        """test if you are creating a Music correctly"""
        self.assertTrue(isinstance(self.music, Music))
        self.assertEquals(Music.objects.count(), 1)
        music = Music.objects.all()[0]
        self.assertEquals(music.name, self.music.name)
        self.assertEquals(music.collectionName, self.music.collectionName)
        self.assertEquals(music.apleId, self.music.apleId)
        self.assertEquals(music.genres.all()[0].name, 'test genre')
        self.assertEquals(music.artists.all()[0].name, 'test artist')
        self.assertEquals(music.price, self.music.price)
        self.assertEquals(music.explicitness, self.music.explicitness)
        self.assertEquals(music.discNumber, self.music.discNumber)
        self.assertEquals(music.trackTimeMillis, self.music.trackTimeMillis)        

    def test_string_representation(self):
        """tests if the presentation is correct"""
        self.assertEqual(str(self.music), self.music.name)
        