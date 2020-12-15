from django.db import IntegrityError
from django.contrib.auth.models import User
from django.db import models
from django.db.models import UniqueConstraint


# from django.urls import reverse


# Create your models here.
class Book(models.Model):
    """
        Model represents Book.
    """

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    objects = models.Manager()
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
    authors = models.ManyToManyField(User, blank=True, related_name="books")
    likes = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(User,
                                        through="manager.LikeBookUser",
                                        blank=True,
                                        related_name="liked_books")

    def __str__(self):
        """Display Book model"""
        return self.title


class LikeBookUser(models.Model):
    """
        Model represents Likes through the ManyToMany link between Book and User models.
    """

    class Meta:
        constraints = [
            UniqueConstraint(fields=['book', 'user'], name='like_unique_book_user')
        ]

    objects = models.Manager()
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="liked_user_table")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_book_table")

    def save(self, **kwargs):
        try:
            super(LikeBookUser, self).save(kwargs)
        except IntegrityError:
            LikeBookUser.objects.get(user=self.user, book=self.book).delete()
            self.book.likes -= 1
        else:
            self.book.likes += 1
        self.book.save()


class Comment(models.Model):
    """
        Model represents user's comment for the book.
    """

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    objects = models.Manager()
    text = models.TextField(max_length=1000,
                            verbose_name="Comment",
                            blank=True,
                            null=True)
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name="comments")
    likes = models.PositiveIntegerField(default=0)
    user_likes = models.ManyToManyField(User,
                                        through="manager.LikeCommentUser",
                                        blank=True, related_name="liked_comments")

    def __str__(self):
        """Display Comment model"""
        return f"Comment: id={self.id} author={self.author}"


class LikeCommentUser(models.Model):
    """
        Model represents Likes through the ManyToMany link between Comment and User models.
    """

    class Meta:
        constraints = [
            UniqueConstraint(fields=["comment", "user"], name="like_unique_comment_user")
        ]

    objects = models.Manager()
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="liked_user_table")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_comment_table")

    def save(self, **kwargs):
        try:
            super(LikeCommentUser, self).save(kwargs)
        except IntegrityError:
            LikeCommentUser.objects.get(user=self.user, comment_id=self.comment).delete()
            self.comment.likes -= 1
        else:
            self.comment.likes += 1
        self.comment.save()
