from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
import uuid  # for unique book instances

from accounts.models import User

# from django.contrib.auth.models import User

# from accounts import
# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    description = models.TextField()
    release_date = models.DateField()
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField("Genre", help_text="Select a genre for this book")
    cover = models.ImageField(upload_to="book/bookcovers", blank=True, null=True)

    def display_genre(self):
        return ",".join(genre.name for genre in self.genre.all())

    display_genre.short_description = "Genre"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

    class Meta:
        ordering = ["title"]


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": str(self.id)})

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class BookInstance(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True, blank=True)
    user = models.ForeignKey(
        "accounts.User", on_delete=models.RESTRICT, null=True, blank=True
    )
    date_updated = models.DateTimeField(auto_now_add=True)

    BOOK_STATUS = {("r", "read"), ("w", "want to read"), ("cr", "currently reading")}

    status = models.CharField(
        max_length=2,
        choices=BOOK_STATUS,
        blank=True,
        default="w",
        help_text="Book status",
    )

    class Meta:
        permissions = (
            ("can mark as read", "read"),
            ("can mark as want to read", "want to read"),
            ("can mark as currently reading", "currently reading"),
        )
        constraints = [
            models.UniqueConstraint(
                fields=["book", "user"], name="uq_bookinstance_book_user"
            )
        ]

    def __str__(self):
        return f"({self.book.title})"


class BooksUser(models.Model):
    title = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
