"""
/manager/ urls're here.
"""
from django.urls import path

from manager.views import hello

# Test mapping url <-> view
urlpatterns = [
    path('<str:name>', hello)
]
