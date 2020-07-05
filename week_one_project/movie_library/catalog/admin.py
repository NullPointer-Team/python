from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'year')

admin.site.register(Movie, MovieAdmin)
