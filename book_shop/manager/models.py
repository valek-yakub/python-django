from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Book(models.Model):
    """
        Model represents Book.
    """

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    title = models.CharField(max_length=50,
                             verbose_name="Title",  # Display in Admin site.
                             help_text="Enter a title of the book."
                             )
    date = models.DateTimeField(verbose_name="Date",
                                auto_now_add=True,
                                null=True
                                )
    summary = models.TextField(max_length=1000,
                               verbose_name="Summary",
                               help_text="Enter a short description of the book.",
                               null=True,
                               blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
        Model represents user's comment for the book.
    """

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    text = models.TextField(max_length=1000,
                            verbose_name="Comment",
                            blank=True,
                            null=True
                            )
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Comment: id={self.id} author={self.author}"
