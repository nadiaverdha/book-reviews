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


def home(request):

    book_list = Book.objects.all()
    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_visits": num_visits,
        "book_list": book_list,
        "col1": book_list[:5],
        "col2": book_list[5:],
    }

    return render(request, "pages/home.html", context=context)


@login_required
def UserBookList(request):
    book_instance = BookInstance.objects.filter(user=request.user)
    template_name: str = "pages/bookinstancelist_user.html"
    paginate_by: int = 4
    context = {"book_instance": book_instance}

    return render(request, "pages/bookinstancelist_user.html", context=context)


def book_detail(request, book_title):
    book = Book.objects.filter(title__icontains=book_title)
    context = {"book": book}
    return render(request, "book-detail", context)


class BookListView(ListView):
    model = Book
    template_name = "pages/book_list.html"

    def get_queryset(self):

        query = self.request.GET.get("q")
        if query:
            book_list = Book.objects.filter(title__icontains=query)
            print(query)
            return book_list


@login_required
def mark_book(request):
    user = request.user
    form = MarkBooks(request.POST)

    if request.method == "POST":
        if form.is_valid():
            bookuser = form.save(commit=True)
            bookuser.user = request.user
            bookuser = form.save(commit=True)

        return HttpResponseRedirect(reverse("profile"))
    else:
        form = MarkBooks()

    context = {"form": form}
    return render(request, "pages/markbooks.html", context)


# #THIS WORKS
# @login_required
# def mark_book(request):
#     print(request)
#     if request.method == "POST":
#         print(request)
#         form = MarkBooks(request.POST)
#         if form.is_valid():
#             bookuser = form.save(commit=True)

#         return HttpResponseRedirect(reverse("my-books"))
#     else:
#         form = MarkBooks()

#     context = {"form": form}
#     return render(request, "pages/markbooks.html", context)
