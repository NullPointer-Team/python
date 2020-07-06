from django.shortcuts import render
from django.views.generic import TemplateView
from .services import get_movies

# Create your views here.
class GetMovie(TemplateView):
    template_name = 'movies.html'
    def get_context_data(self, *args, **kwargs):
        context = {
            'movies': get_movies(),
        }
        return context
