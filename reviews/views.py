from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views import generic
from .models import Reviews
from book.models import Book

# def home(request):
#     return render(request, "reviews.html")


def reviews(request):

    books = Book.objects.all()
    all_reviews = Reviews.objects.all()

    context = {
        "books": books,
        "all_reviews": all_reviews,
    }

    return render(request, "reviews/reviews.html", context=context)
