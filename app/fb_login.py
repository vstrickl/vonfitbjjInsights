"""Sets Up OAuth Login for Facebook."""

import logging
import random
import string
import requests

from decouple import config
from vonfitbjjInsights.settings import BASE_URL
logging.basicConfig(level=logging.INFO, format='%(message)s')

CALLBACK_URL = f"{BASE_URL}/callback"

def generate_state():
    """Generates a random state for OAuth."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

def invoke_login():
    """Invokes the Facebook Login."""
    url = 'https://www.facebook.com/v20.0/dialog/oauth?'
    params = {
        'client_id': config('FACEBOOK_APP_ID'),
        'redirect_uri': CALLBACK_URL,
        'state': generate_state(),
        'response_type': 'code',
        'scope': 'public_profile,email' 
    }

    try:
        request_url = requests.Request('GET', url, params=params).prepare().url
        logging.info('\nRequest Successful.')
        return request_url
    except requests.exceptions.RequestException as req_err:
        logging.error('Request error occurred: %s', req_err)
    except Exception as err:
        logging.error('An error occurred: %s', err)

if __name__ == "__main__":
    login_url = invoke_login()
    if login_url:
        logging.info('\nVisit the following URL to log in:\n')
        logging.info(login_url)
