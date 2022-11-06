from django.shortcuts import render
from django.views import generic
from .models import Book, Author, Genre

# Create your views here.


class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"

    queryset = Book.objects.all()
