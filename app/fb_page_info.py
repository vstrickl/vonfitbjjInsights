# type: ignore
"""Grabs Facebook Page Info for Account."""

import logging

from setup_env import setup_django_environment
from setup_env import setup_logging

# Set up Django environment and logging
setup_django_environment()
logger = setup_logging()

# pylint: disable=wrong-import-position
# ruff: noqa: E402
from metainsights.models import FacebookToken
from metainsights.fb_utils import clean_page_info
from metainsights.fb_info import get_facebook_pages
from metainsights.fb_utils import save_page_info_to_db

# Call Function
if __name__ == "__main__":
    try:
        latest_token_entry = FacebookToken.objects.latest('created_at')  # pylint: disable=no-member
        access_token = latest_token_entry.token
        page_info = get_facebook_pages(access_token)
        if page_info:
            # Remove specific keys
            cleaned_page_info = clean_page_info(page_info)
            save_page_info_to_db(cleaned_page_info)
            logging.info('Page info written to page_info.json')
    except FacebookToken.DoesNotExist:  # pylint: disable=no-member
        logger.error('No access token found.')
