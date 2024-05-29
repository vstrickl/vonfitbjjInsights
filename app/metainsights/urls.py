from django.urls import path

from . import views

# Create your Url patterns here...
urlpatterns = [
    path('', views.fb_login, name='fb_login'),
]