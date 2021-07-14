from django.contrib import admin
from django.urls import path, include
from .views import BookCreateView, BookDetailView
from. import views

urlpatterns = [
    path('', views.index , name="home"),
    path("newbook/", BookCreateView.as_view() , name = "new-book"),
    path('<int:pk>',BookDetailView.as_view(),name='book-detail'),
    path("allbooks/" ,views.allbooks,name="all-books"),
    path("search/", views.SearchBook, name = "search")
]
