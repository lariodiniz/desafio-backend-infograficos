from django.test import TestCase

from model_mommy import mommy
from core.models import Genre

class GenreModelTestCase(TestCase):
    """Testing the model Genre"""

    def setUp(self):
        """Initial Test Settings"""
        self.genre = mommy.make(Genre)

    def tearDown(self):
        """Final method"""
        self.genre.delete()

    def test_there_are_fields(self):
        """test the fields the model"""
        filds = ['name']
        
        for fild in filds:
            self.assertTrue(fild in dir(Genre),
                            'Class Genre does not have the field {}'.format(fild))

    def test_there_is_a_genre(self):
        """test if you are creating a Genre correctly"""
        self.assertTrue(isinstance(self.genre, Genre))
        self.assertEquals(Genre.objects.count(), 1)
        self.assertEquals(Genre.objects.all()[0].name, self.genre.name)

    def test_string_representation(self):
        """tests if the presentation is correct"""
        self.assertEqual(str(self.genre), 'Genre {}'.format(self.genre.name))
        