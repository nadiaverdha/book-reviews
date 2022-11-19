from django.shortcuts import render
from .models import User
from book.models import BookInstance
from reviews.models import Reviews

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
    user_books = BookInstance.objects.filter(user=request.user).distinct()
    user_reviews = Reviews.objects.filter(user=request.user)

    context = {
        "username": username,
        "email": email,
        "date": date,
        "image": image,
        "no_books": no_books,
        "image": image,
        "user_reviews": user_reviews,
        "user_books": user_books,
    }
    return render(request, "accounts/profile.html", context=context)
