from django.db import models
from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
import uuid  # for unique book instances

from accounts.models import User
from book.models import Book, BookInstance


# Create your models here.


class Reviews(models.Model):

    STATUS = ((0, "Draft"), (1, "Publish"))
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="reviews"
    )
    book = models.ForeignKey("book.Book", on_delete=models.RESTRICT)
    created_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title
