from django.core.management.base import BaseCommand
from manager.models import Book


class Command(BaseCommand):
    """
        Class is used to prevent the previous backward problem caused by the update like's mechanism.
    """

    def handle(self, *args, **options):
        books = Book.objects.all()
        for book in books:
            book.rate_stars_num = int(book.users_rate_score)
            book.save()
