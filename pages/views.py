from django.shortcuts import render
from book.models import Book, Author, Genre, BookInstance
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import permission_required


def home(request):

    num_books = Book.objects.all().count()
    num_authors = Author.objects.all().count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_authors": num_authors,
        "num_visits": num_visits,
    }

    return render(request, "pages/home.html", context=context)


class UserBookList(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name: str = "pages/bookinstancelist_user.html"
    paginate_by: int = 4

    def get_queryset(self):
        return BookInstance.objects.filter(user=self.request.user)
