from django.db.models import Count, Prefetch
from django.shortcuts import render, redirect

# Create your views here.

from django.views import View
from manager.models import Book, Comment, LikeBookUser, LikeCommentUser


class MyPage(View):

    @staticmethod
    def get(request):
        # TODO: prefetch for comment's fields
        # lu_comment_count = Comment.objects.annotate()
        # comments_prefetch = Prefetch()
        context = {
            "books": Book.objects.prefetch_related("authors", "comments").annotate(likes_count=Count("likes"),
                                                                                   comments_count=Count("comments")),
        }
        return render(request, "index.html", context)


class AddLikeBook(View):

    @staticmethod
    def get(request, id):
        if request.user.is_authenticated:
            LikeBookUser.objects.create(user=request.user, book_id=id)

        return redirect("the-main-page")


class AddLikeComment(View):

    @staticmethod
    def get(request, id):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id)

        return redirect("the-main-page")