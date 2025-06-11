from django.shortcuts import render

from django.views.generic import ListView
from .models import Comic
# Create your views here.
class ComicList(ListView):
    model = Comic
    template_name = 'comics.html'
    context_object_name = 'comics'
