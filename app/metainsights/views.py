import logging
import requests
from django.http import HttpResponse
from django.http import HttpResponseBadRequest
from decouple import config

from .models import FacebookToken

logging.basicConfig(level=logging.INFO, format='%(message)s')
BASE_URL = config('BASE_URL')
CALLBACK_URL = f"{BASE_URL}/callback"

# Create your views here.
def callback(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponseBadRequest('Authorization failed.')

    access_token = exchange_code_for_token(code)
    if access_token:
        save_token(access_token)
        return HttpResponse('Login successful. You can now use the command line tool.')
    else:
        return HttpResponse('Failed to obtain access token.')

def exchange_code_for_token(code):
    url = 'https://graph.facebook.com/v20.0/oauth/access_token'
    params = {
        'client_id': config('FACEBOOK_APP_ID'),
        'redirect_uri': CALLBACK_URL,
        'client_secret': config('FACEBOOK_APP_SECRET'),
        'code': code
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['access_token']
    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error(f'An error occurred: {err}')
    return None

def save_token(access_token):
    try:
        token_entry = FacebookToken(token=access_token)
        token_entry.save()
        logging.info('Access token saved successfully.')
    except Exception as err:
        logging.error(f'Error saving access token: {err}')