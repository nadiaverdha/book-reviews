from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
]

urlpatterns += [
    path("mybooks", views.UserBookList.as_view(), name="my-books"),
]
