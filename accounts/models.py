from logging.config import IDENTIFIER
from django.db import models
from django.contrib.auth.models import AbstractUser

# from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class User(AbstractUser):

    email = models.CharField(max_length=500)
    # firstname = models.CharField(max_length=500)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
