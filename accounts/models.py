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
    def __str__(self):
        return self.username
