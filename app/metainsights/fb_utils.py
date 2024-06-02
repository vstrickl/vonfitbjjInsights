import requests
import logging
from .models import FacebookPage

# Create Facebook Utils here.
def get_facebook_pages(access_token):
    url = f"https://graph.facebook.com/v20.0/me/accounts"

    try:
        response = requests.get(url, params={'access_token': access_token})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error(f'An error occurred: {err}')

def clean_page_info(page_info):
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
    if 'data' in cleaned_page_info:
        for page in cleaned_page_info['data']:
            FacebookPage.objects.update_or_create(
                page_id=page['id'],
                defaults={
                    'name': page['name'],
                    'category': page['category'],
                    'category_list': page['category_list']
                }
            )