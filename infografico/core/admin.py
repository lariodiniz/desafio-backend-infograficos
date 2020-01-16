__author__ = "Lário dos Santos Diniz"


from django.contrib import admin

from .models import Album, Artist, Genre, Music

admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Music)
