"""This module generates the URL Paths for the Home App."""
from django.urls import path

from . import views

# Create your Url patterns here...
urlpatterns = [
    path('', views.home, name='home'),
]
