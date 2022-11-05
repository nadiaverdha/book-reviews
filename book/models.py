from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
import uuid  # for unique book instances

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
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
    cover = models.ImageField(upload_to="book/bookcovers", blank=True, null=True)

    def display_genre(self):
        return ",".join(genre.name for genre in self.genre.all())

    display_genre.short_description = "Genre"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])

    # #creating the bookinstance model that shows information on specific books

    #     class BookInstance(models.Model):
    #         id = models.UUIDField(primary_key = True, default=uuid.uuid4, help_text ="Unique id for the particular book")

    #         book = models.ForeignKey('Book', on_delete = models.RESTRICT,null= True)

    #         READING_STATUS = (
    #             ('w', 'want to read'),
    #             ('r','read'),
    #             ('rc','reading')
    #         )

    #         status = models.CharField(
    #             max_length = 1,
    #             choices = READING_STATUS,
    #             blank = True,
    #             default = None,
    #             help_text = 'Book reading status'
    #         )


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"
