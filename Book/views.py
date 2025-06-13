from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Comic


# Create your views here.
class ComicList(ListView):
    model = Comic
    template_name = 'comics.html'
    context_object_name = 'comics'

    # Detail view 
class ComicDetails(DetailView):
    model = Comic
    template_name = 'comic-details.html'
    context_object_name = 'comic'

# 3. Update view (Update statement)
class EditComic(UpdateView):
    model = Comic
    fields = '__all__'
    template_name = 'comic-edit.html'
    success_url = '/'

# 4. Delete view (Delete statement)
class DeleteComic(DeleteView):
    model = Comic
    template_name = 'comic-delete.html'
    success_url = '/'