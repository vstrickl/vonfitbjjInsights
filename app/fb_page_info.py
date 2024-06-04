import os
import django
import logging

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vonfitbjjInsights.settings')
django.setup()

from metainsights.models import FacebookToken
from metainsights.fb_utils import clean_page_info
from metainsights.fb_info import get_facebook_pages
from metainsights.fb_utils import save_page_info_to_db

# Set up logging
logger = logging.getLogger('metainsights')
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Call Function
if __name__ == "__main__":
    try:
        latest_token_entry = FacebookToken.objects.latest('created_at')
        access_token = latest_token_entry.token
        page_info = get_facebook_pages(access_token)
        if page_info:
            # Remove specific keys
            cleaned_page_info = clean_page_info(page_info)
            save_page_info_to_db(cleaned_page_info)
            logging.info('Page info written to page_info.json')
    except FacebookToken.DoesNotExist:
        logger.error('No access token found.')
    except Exception as err:
        logger.error(f'An error occurred: {err}')
