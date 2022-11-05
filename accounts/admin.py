from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import User

# Register your models here.


from .forms import UserCreationForm, UserChangeForm
from .models import User

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm

    model = User

    list_display = ["email", "username"]


admin.site.register(User, CustomUserAdmin)
