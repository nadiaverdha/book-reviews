from django.contrib import admin

# Register your models here.


from .models import Book, Author, Genre, BookInstance


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "birthdate")


# admin.site.register(Author, AuthorAdmin)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "description", "display_genre", "release_date"]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("id", "book", "status", "user")
    list_filter = ["status"]


@admin.register(Genre)
class AdminGenre(admin.ModelAdmin):
    pass
