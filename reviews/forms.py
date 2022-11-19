from django import forms
from django.forms import ModelForm
from reviews.models import Reviews
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class PostReviews(ModelForm):
    class Meta:
        model = Reviews
        fields = "__all__"
