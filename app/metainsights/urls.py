"""This module generates the URL Paths for Meta Insights."""
from django.urls import path

from . import views

# Create your Url patterns here...
urlpatterns = [
    path('callback/', views.callback, name='callback'),
]
