import requests
import logging

from .models import FacebookPage

# Create Functions here.
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

def ig_account_info(access_token, page_id):
    url = f"https://graph.facebook.com/v20.0/{page_id}"
    params={
        "fields": "instagram_business_account",
        'access_token': access_token
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error(f'An error occurred: {err}')

def get_page_id_by_cli_name(cli_name):
    try:
        page = FacebookPage.objects.get(cli_name=cli_name)
        return page.page_id
    except FacebookPage.DoesNotExist:
        logging.error(f"No FacebookPage found with cli_name: {cli_name}")
    return None

def update_ig_user_id(cli_name, ig_user_id):
    try:
        page = FacebookPage.objects.get(cli_name=cli_name)
        page.ig_user_id = ig_user_id
        page.save()
        logging.info(f"Successfully updated {cli_name} FacebookPage model!")
    except FacebookPage.DoesNotExist:
        logging.error(f"No FacebookPage found with cli_name: {cli_name}")