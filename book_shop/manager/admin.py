from django.contrib import admin

# Register your models here.
from manager.models import Book, Comment


# Inline classes
class CommentInline(admin.TabularInline):
    """
        Class represents Comment in the Book Admin site.
    """
    model = Comment
    extra = 0


# Main classes
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "date")
    inlines = [CommentInline]

