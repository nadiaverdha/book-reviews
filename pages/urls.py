from django.urls import path

from . import views
from .views import BookListView

urlpatterns = [
    path("", views.home, name="home"),
]

urlpatterns += [
    path("mybooks", views.UserBookList, name="my-books"),
]

urlpatterns += [
    path("book/", views.book_detail, name="book-detail"),
]

urlpatterns += [
    path("bookstatus/", views.mark_book, name="mark-book-status"),
]

urlpatterns += [
    path("books/", BookListView.as_view(), name="book-list"),
]
