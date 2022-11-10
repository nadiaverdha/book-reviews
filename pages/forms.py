from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class MarkBooks(forms.Form):
    book_status = forms.ChoiceField(
        label="book_status", initial="want to read", help_text="Mark book"
    )
