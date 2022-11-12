from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
]

urlpatterns += [
    path("mybooks", views.UserBookList, name="my-books"),
]

urlpatterns += [
    path("bookstatus/", views.mark_book, name="mark-book-status"),
]


urlpatterns += [
    path("books", views.BookListView, name="book-list"),
]
