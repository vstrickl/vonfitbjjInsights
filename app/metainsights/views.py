from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fb_login(request):

    if request.user.is_authenticated:
        context = {
            'heading': 'Logout',
            'desc': 'You are authenticated with Facebook.'
        }
    else:
        context = {
            'heading': 'Login',
            'desc': 'Authenticate with Facebook'
        }

    return render(request, 'login.html', context)

def fb_redirect(request):
    if request.user.is_authenticated:
        return HttpResponse('You are successfully logged in and authenticated with Facebook.')
    else:
        return HttpResponse('You are successfully logged out of Facebook.')