from django.shortcuts import render
from book.models import Book, Author, Genre
from django.views import generic

# Create your views here.


def home(request):

    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
    }

    return render(request, "pages/home.html", context=context)
