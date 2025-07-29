from django.urls import path

from . import views

urlpatterns = [

    path('', views.homeView, name = 'homepage'),
    path('comic/<int:pk>', views.ComicDetails.as_view(), name='comic_details'),
    path('comic/add',views.AddComic.as_view(),name ='add_comic'),
    path('comic/edit/<int:pk>', views.EditComic.as_view(), name = 'edit_comic'),
    path('comic/del/<int:pk>', views.DeleteComic.as_view(), name = 'del_comic'),
    path('comics/search',views.searchView,name ='search'),
    path('comics/mycomics', views.myBooks, name = 'mybooks'),
    path('comics/read/<int:id>', views.readBook, name = 'read_comic')
]


