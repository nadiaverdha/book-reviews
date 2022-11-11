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


def home(request):

    num_books = Book.objects.all().count()
    inst = BookInstance.objects.all()
    books = Book.objects.all()
    num_authors = Author.objects.all().count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_visits": num_visits,
    }

    return render(request, "pages/home.html", context=context)


def UserBookList(request):
    book_instance = BookInstance.objects.all()
    template_name: str = "pages/bookinstancelist_user.html"
    paginate_by: int = 4
    context = {"book_instance": book_instance}

    return render(request, "pages/bookinstancelist_user.html", context=context)


def BookListView(request):
    # model = Book
    # context_object_name = "book_list"
    num_books = Book.objects.all().count()
    book_list = Book.objects.all()
    context = {"book_list": book_list, "num_books": num_books}

    return render(request, "pages/book_list.html", context=context)


@login_required
def mark_book(request):
    # book_instance = BookInstance
    book_instance = BookInstance.objects.all()
    # for book in books:
    # If this is a POST request then process the Form data
    for b in book_instance:
        if request.method == "POST":

            # Create a form instance and populate it with data from the request (binding):
            form = MarkBooks(request.POST)

            if form.is_valid():
                # book_instance.book.title = book.title
                b.user = request.user
                b.status = form.cleaned_data["status"]
                b.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse("my-books"))

    else:
        proposed_status = "want to read"
        form = MarkBooks(initial={"status": proposed_status})

    context = {
        "form": form,
        "b": book_instance,
    }

    return render(request, "pages/markbooks.html", context)


# def mark_book(request):

#     if request.method == "POST":
#         form = MarkBooks(request.Post)
#     else:
#         form = MarkBooks()

#     return render(request, "pages/markbooks.html")
