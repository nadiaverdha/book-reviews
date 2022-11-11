from django import forms
from django.forms import ModelForm
from book.models import BookInstance
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

BOOK_STATUS = {("r", "read"), ("w", "want to read"), ("cr", "currently reading")}


class MarkBooks(forms.Form):
    status = forms.ChoiceField(
        choices=BOOK_STATUS,
        label="",
        initial="want to read",
    )

    def clean_book_status(self):
        data = self.cleaned_data["book_status"]

        # Check if a date is not in the past.
        if data not in BOOK_STATUS:
            raise ValidationError(_("invalid"))

        # Remember to always return the cleaned data.
        return data
