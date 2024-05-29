import os
import django
import logging
import requests
from vonfitbjjInsights import settings

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vonfitbjjInsights.settings')
django.setup()

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_facebook_pages(access_token):
    url = f"https://graph.facebook.com/v20.0/me/accounts?access_token={access_token}"
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    # Hard-coded access token for testing purposes (replace with a valid token)
    access_token = settings.AT
    pages = get_facebook_pages(access_token)
    logger.info(f"Retrieved Facebook pages: {pages}")
    print(pages)
