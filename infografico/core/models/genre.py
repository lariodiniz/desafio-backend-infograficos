__author__ = "Lario dos Santos Diniz"

from django.db import models
from django.utils.translation import gettext as _

class Genre(models.Model):
    """Genre model class"""
    
    name = models.CharField(verbose_name=_('Name'),max_length=30, unique=True)
    
    class Meta:
        verbose_name = _('Genre')
        verbose_name_plural = _('Genres')

    def __str__(self):
        return _('Genre {}'.format(self.name))
