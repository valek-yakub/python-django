"""
/manager/ urls're here.
"""
from django.urls import path

from manager.views import MyPage, AddLikeBook, AddLikeComment

urlpatterns = [
    path("add_like_book/<int:id>/", AddLikeBook.as_view(), name="add-like-book"),
    path("add_like_comment/<int:id>/", AddLikeComment.as_view(), name="add-like-comment"),
    path('', MyPage.as_view(), name="the-main-page"),
]
