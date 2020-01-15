from django.test import TestCase

from model_mommy import mommy
from core.models import Genre, Artist, Album

class AlbumModelTestCase(TestCase):
    """Testing the model Album"""

    def setUp(self):
        """Initial Test Settings"""
        self.genre = mommy.make(Genre, name='test genre')
        self.artist = mommy.make(Artist, name='test artist', genres=[self.genre])
        self.album = mommy.make(Album, genres=[self.genre], artists=[self.artist])

    def tearDown(self):
        """Final method"""
        self.artist.delete()
        self.genre.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name', 'collectionName', 'apleId','genres','artists']
        
        for fild in filds:
            self.assertTrue(fild in dir(Album),
                            'Class Album does not have the field {}'.format(fild))

    def test_there_is_a_album(self):
        """test if you are creating a Album correctly"""
        self.assertTrue(isinstance(self.album, Album))
        self.assertEquals(Album.objects.count(), 1)
        album = Album.objects.all()[0]
        self.assertEquals(album.name, self.album.name)
        self.assertEquals(album.apleId, self.album.apleId)
        self.assertEquals(album.genres.all()[0].name, 'test genre')
        self.assertEquals(album.artists.all()[0].name, 'test artist')

    def test_string_representation(self):
        """tests if the presentation is correct"""
        self.assertEqual(str(self.album), self.album.name)
        