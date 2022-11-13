from django.shortcuts import render
from .models import User
from book.models import BookInstance

# Create your views here.


def profile(request):

    username = request.user
    # email = username.email

    email = User.objects.values("email").filter(username=username)[0]["email"]
    date = User.objects.values("date_joined").filter(username=username)[0][
        "date_joined"
    ]
    image = User.objects.values("image").filter(username=username)[0]["image"]
    no_books = BookInstance.objects.filter(user=request.user).count()
    shelf = BookInstance.objects.filter(user=request.user).all()
    context = {
        "username": username,
        "email": email,
        "date": date,
        "image": image,
        "no_books": no_books,
        "shelf": shelf,
        "image": image,
    }
    return render(request, "accounts/profile.html", context=context)
