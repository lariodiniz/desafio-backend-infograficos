__author__ = "Lario dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext as _

from core.models import Genre, Artist

class Album(models.Model):
    """Album model class"""
    
    name = models.CharField(verbose_name=_('Name'),max_length=50)
    collectionName = models.CharField(verbose_name='collectionName',max_length=50)
    apleId = models.IntegerField('apleId')
    genres = models.ManyToManyField(Genre, verbose_name=_('Genres'), blank=True)
    artists = models.ManyToManyField(Artist, verbose_name=_('Artists'), blank=True)
    
    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')

    def __str__(self):
        return self.name
