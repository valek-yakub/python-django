"""
/manager/ urls're here.
"""
from django.urls import path

from manager.views import MainPage, AddLikeComment, AddRateBook

urlpatterns = [
    path("add_like_comment/<int:id>/", AddLikeComment.as_view(), name="add-like-comment"),
    path("add_rate_book/<int:id>/<int:rate>/", AddRateBook.as_view(), name="add-rate-book"),
    path('', MainPage.as_view(), name="the-main-page"),
]
