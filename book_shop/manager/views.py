from django.db.models import Count, Prefetch
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from manager.models import Book, Comment, LikeBookUser, LikeCommentUser


# class MyPage(View):
#
#     @staticmethod
#     def get(request):
#         context = {}
#
#         lu_comment_count = Comment.objects.annotate(likes_count=Count("user_likes"))
#         lu_comment_count = lu_comment_count.select_related("author")
#         comments_prefetch = Prefetch("comments", queryset=lu_comment_count)
#         books = Book.objects.prefetch_related(comments_prefetch)
#
#         context["books"] = books.annotate(likes_count=Count("user_likes"))
#
#         return render(request, "index.html", context)


class MyPage(View):

    @staticmethod
    def get(request):
        context = {}

        # lu_comment_count = Comment.objects.annotate(likes_count=Count("user_likes"))
        # lu_comment_count = lu_comment_count.select_related("author")
        query_comments_sel_author = Comment.objects.select_related("author")
        comments_prefetch = Prefetch("comments", queryset=query_comments_sel_author)
        books = Book.objects.prefetch_related(comments_prefetch)

        context["books"] = books

        return render(request, "index.html", context)


class AddLikeBook(View):

    @staticmethod
    def get(request, id):
        if request.user.is_authenticated:
            print(request.path)
            LikeBookUser.objects.create(user=request.user, book_id=id)

        return redirect("the-main-page")


class AddLikeComment(View):

    @staticmethod
    def get(request, id):
        if request.user.is_authenticated:
            LikeCommentUser.objects.create(user=request.user, comment_id=id)

        return redirect("the-main-page")
