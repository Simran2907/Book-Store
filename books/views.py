from django.db.models import fields
from django.db.models.base import Model
from django.db.models.fields import files
from django.shortcuts import render
from django.views.generic import CreateView,DetailView
from .models import Book


def index(request):
	return render(request, "index.html")

class BookCreateView(CreateView):
	model = Book
	fields = ['book', 'author', 'genre','language']

	def form_valid(self, form):
		return super().form_valid(form)

class BookDetailView(DetailView):
	model = Book

def allbooks(request):
	context = {
		'books': Book.objects.all()
	}
	return render(request,"allbooks.html",context)

def SearchBook(request):
	qs = Book.objects.all()
	s_genre = request.GET.get('book_genre')
	s_lang = request.GET.get('book_language')
	langs = []
	genres = []
	if s_genre:
		genres = [x.strip() for x in s_genre.split(',')]
		result = []
		for book in qs:
			for book_genre in book.genre:
				if book_genre in genres:
					result.append(book)
	
		context = {
			'queryset': result
		}
		return render(request, "search.html", context)
	
	if s_lang:
		langs = [x.strip() for x in s_lang.split(',')]
		result = []
		for book in qs:
			for book_language in book.language:
				if book_language in langs:
					result.append(book)
	
		context = {
			'queryset': result
		}
		return render(request, "search.html", context)
	
	context={
	   'queryset':qs
	}
	return render(request,"search.html", context)