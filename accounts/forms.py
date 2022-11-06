from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django.contrib.auth import password_validation
from django.contrib.auth import get_user_model


from .models import User


# class UserCreationForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ("username", "email")


# class UserChangeForm(UserChangeForm):
#     model = User
#     field = ("username", "email")
User = get_user_model()


# class RegistrationForm(forms.Form):
#     username = forms.CharField(max_length=32, required=True)
#     password = forms.CharField(
#         max_length=128, min_length=8, required=True, widget=forms.PasswordInput
#     )
#     password_confirm = forms.CharField(
#         max_length=128, min_length=8, widget=forms.PasswordInput
#     )

#     def clean_username(self):
#         username = self.cleaned_data["username"]

#         try:
#             User.objects.get(username=username)

#         except User.DoesNotExist:
#             return username
#         else:
#             raise ValidationError("Username is already taken")

#     def clean_password(self):
#         password = self.cleaned_data["password"]
#         password_validation.validate_password(password)
#         return password

#     def clean(self):
#         password = self.cleaned_data.get("password")
#         password_confirm = self.cleaned_data.get("password_confirm")
#         if password is None or password_confirm != password:
#             raise ValidationError("Password does not match")

#         return self.cleaned_data
