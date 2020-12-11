from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

from manager.models import Book


class MyPage(View):

    @staticmethod
    def get(request):
        context = {
            "name": "Valek",
            "addr": "Minsk",
            "arr": ["Igor", "Fedya", "Petya", "Valek", "George", "Oleg"],
            "books": Book.objects.all(),
        }
        return render(request, "index.html", context)
