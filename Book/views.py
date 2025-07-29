from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import JsonResponse

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Comic
from orders.models import Order, OrderDetails
from django.contrib.auth.mixins import LoginRequiredMixin

# CRUD operations of Comic model

# 1. Create(Instart statements)

class AddComic(LoginRequiredMixin,CreateView):
    model = Comic
    fields = '__all__'
    template_name = 'add_comic.html'
    success_url = '/'

# 2. Read (statements)
# List view
def homeView(request):
    comics=Comic.objects.all()   # SELECT * FROM mainapp_product;
    context={
        'comics' : comics,
        'search_bar' :True
    }
    template='home.html'
    return render(request, template, context)   # this renders the response according to the request using the context


    # Detail view 
class ComicDetails(DetailView):
    model = Comic
    template_name = 'comic-details.html'
    context_object_name = 'comic'
    success_url = '/'

# 3. Update view (Update statement)
class EditComic(LoginRequiredMixin, UpdateView):
    model = Comic
    fields = '__all__'
    template_name = 'comic-edit.html'
    success_url = '/'


# # Create your views here.
# class ComicList(ListView):
#     model = Comic
#     template_name = 'comics.html'
#     context_object_name = 'comics'


# 4. Delete view (Delete statement)
class DeleteComic(DeleteView):
    model = Comic
    template_name = 'comic-delete.html'
    context_object_name = "Comic"
    success_url = '/'



# class AddCart(CreateView):
#     model=Comic
#     fields='__all__'
#     template_name=''

def searchView(request):
    query=request.Get.get('search_text')

    result_products = Comic.objects.filter(name_iconstains =query)
    context = {
        'comics' : (searchView),
        'query' : query,
        'search_bar' :True
    }

    template = loader.get_template('search_results.html')
    return HttpResponse(template,render(context,request))


def myBooks(request):
    orders = Order.objects.filter(user = request.user)
    ordered_books = []
    order_items = []
    for order in orders:
        order_items.extend(list(OrderDetails.objects.filter(order = order)))
    for item in order_items:
        ordered_books.append(item.order_item)

    context = {
        'comics' : ordered_books
    }
    template = 'mybooks.html'
    return render(request, template, context) 
        

from django.views.decorators.clickjacking import xframe_options_exempt

@xframe_options_exempt
def readBook(request, id):

    comic = Comic.objects.get(id = id)

    context = {
        'comic' : comic
    }
    template = 'read_comic.html'
    return render(request, template, context) 