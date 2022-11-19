from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views import generic
from .models import Reviews
from reviews.forms import PostReviews
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render
from book.models import Book, Author, Genre, BookInstance
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from pages.forms import MarkBooks
from django.views.generic.edit import FormView
from django.views.generic import TemplateView, ListView

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


@login_required
def reviews_post(request):
    # form = PostReviews(request.POST)
    # if request.method == "POST":
    #     print(form)
    #     if form.is_valid():

    #         reviewuser = form.save(commit=True)
    #         reviewuser.user = request.user
    #         reviewuser = form.save(commit=True)

    #     return HttpResponseRedirect(reverse("postreviews"))
    # else:
    #     form = PostReviews()

    # context = {"form": form}
    # return render(request, "reviews/reviewspost.html", context)
    user = request.user
    form = PostReviews(request.POST)

    if request.method == "POST":
        if form.is_valid():
            bookuser = form.save(commit=True)
            bookuser.user = request.user
            bookuser = form.save(commit=True)

        return HttpResponseRedirect(reverse("profile"))
    else:
        form = PostReviews()

    context = {"form": form}
    return render(request, "reviews/reviewspost.html", context)
