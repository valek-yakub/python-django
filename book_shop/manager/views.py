from django.db.models import Prefetch
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from manager.models import Book, Comment, LikeCommentUser, RateBookUser


class MainPage(View):

    @staticmethod
    def get(request):
        context = {}

        query_comments_sel_author = Comment.objects.select_related("author")
        comments_prefetch = Prefetch("comments", queryset=query_comments_sel_author)
        books = Book.objects.prefetch_related(comments_prefetch)

        context["books"] = books
        context["stars_num"] = range(1, 6)
        # TODO: rate

        return render(request, "index.html", context)


class AddLikeComment(View):

    @staticmethod
    def get(request, id):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id)

        return redirect("the-main-page")


class AddRateBook(View):

    @staticmethod
    def get(request, id, rate):
        if request.user.is_authenticated:
            RateBookUser.objects.create(user=request.user,
                                        book_id=id,
                                        user_rate_score=rate)

        return redirect("the-main-page")
