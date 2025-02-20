"""This module generates the page views for the Home App."""
from django.http import HttpResponse

# Create your views here.
def home(request):
    """Home Page view."""
    return HttpResponse("Welcome to your Market Research Center!")
