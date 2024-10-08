# type: ignore
"""Utilites Function for Facebook"""

import logging

from .models import FacebookPage
from .models import FacebookToken

# Create Facebook Utils here.
def clean_page_info(page_info):
    """Clean Facebook Page Info"""
    # Remove "paging", "tasks", and "access_token" from the JSON data
    if 'paging' in page_info:
        del page_info['paging']
    if 'data' in page_info:
        for page in page_info['data']:
            if 'access_token' in page:
                del page['access_token']
            if 'tasks' in page:
                del page['tasks']
    return page_info

def save_page_info_to_db(cleaned_page_info):
    """Save Facebook Page Info to Database"""
    if 'data' in cleaned_page_info:
        for page in cleaned_page_info['data']:
            FacebookPage.objects.update_or_create(  # pylint: disable=no-member
                page_id=page['id'],
                defaults={
                    'name': page['name'],
                    'category': page['category'],
                    'category_list': page['category_list']
                }
            )

def get_latest_access_token():
    """Get Latest Facebook Access Token"""
    try:
        token = FacebookToken.objects.latest('updated_at')  # pylint: disable=no-member
        return token.token
    except FacebookToken.DoesNotExist:  # pylint: disable=no-member
        logging.error("No access token found.")
    return None