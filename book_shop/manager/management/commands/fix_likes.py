from django.core.management.base import BaseCommand
from django.db.models import Count

from manager.models import Book, Comment


class Command(BaseCommand):
    """
        Class is used to prevent the previous backward problem caused by the update like's mechanism.
    """

    def handle(self, *args, **options):
        books = Book.objects.annotate(count_likes=Count("user_likes"))
        comments = Comment.objects.annotate(count_likes=Count("user_likes"))
        for book, comment in zip(books, comments):
            book.likes = book.count_likes
            comment.likes = comment.count_likes
        Book.objects.bulk_update(books,
                                 fields=['likes'],
                                 batch_size=3)
        Comment.objects.bulk_update(books,
                                    fields=['likes'],
                                    batch_size=3)
        # print([(i.likes, i.count_likes) for i in comments])
