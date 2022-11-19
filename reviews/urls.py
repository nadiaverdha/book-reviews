from . import views

from django.urls import path
from .views import reviews_post

urlpatterns = [
    path("reviews", views.reviews, name="reviews"),
    path("reviews/postreviews", views.reviews_post, name="postreviews"),
]
