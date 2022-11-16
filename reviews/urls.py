from . import views
from django.urls import path


urlpatterns = [
    path("reviews", views.reviews, name="reviews"),
]
