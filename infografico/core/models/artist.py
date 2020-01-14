__author__ = "Lario dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext as _

from core.models import Genre

class Artist(models.Model):
    """Artist model class"""
    
    name = models.CharField(verbose_name=_('Name'),max_length=50)
    apleId = models.IntegerField('apleId')
    genres = models.ManyToManyField(Genre, verbose_name=_('Genres'), blank=True)
    
    class Meta:
        verbose_name = _('Artist')
        verbose_name_plural = _('Artists')

    def __str__(self):
        return self.name
