from django.contrib import admin

# Register your models here.

from .models import Reviews


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on", "book", "user", "content")
    list_filter = ("status",)
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
