__author__ = "Lario dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext as _

from core.models import Genre, Artist

class Album(models.Model):
    """Album model class"""
    
    EXPLICITNESS_CHOICES = (
        (0, _('Not Explicit')),
        (1, _('Explicit')),
    )
    
    name = models.CharField(verbose_name=_('Name'),max_length=50)
    collectionName = models.CharField(verbose_name='collectionName',max_length=50)
    apleId = models.IntegerField('apleId')
    genres = models.ManyToManyField(Genre, verbose_name=_('Genres'), blank=True)
    artists = models.ManyToManyField(Artist, verbose_name=_('Artists'), blank=True)
    price = models.DecimalField(verbose_name=_('Price'), decimal_places=2, max_digits=20)
    explicitness = models.IntegerField(verbose_name=_('Explicitness'), choices=EXPLICITNESS_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = _('Album')
        verbose_name_plural = _('Albums')

    def __str__(self):
        return self.name
