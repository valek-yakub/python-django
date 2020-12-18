from django.core.management.base import BaseCommand
from manager.models import Book


class Command(BaseCommand):
    """
        Class is used to prevent the previous backward problem caused by the update like's mechanism.
    """

    def handle(self, *args, **options):
        books = Book.objects.all()
        for book in books:
            book.users_rate_count = 0
            book.users_rate_score = 0
            book.save()
