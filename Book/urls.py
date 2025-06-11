from django.urls import path
from . import views

urlpatterns = [

    path('', views.ComicList.as_view(), name = 'home')
]