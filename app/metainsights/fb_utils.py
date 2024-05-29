import os
import django
import logging
import requests

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vonfitbjjInsights.settings')
django.setup()

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Create your functions here.
def get_facebook_pages(access_token):
    url = f"https://graph.facebook.com/v20.0/me/accounts?access_token={access_token}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    get_facebook_pages()