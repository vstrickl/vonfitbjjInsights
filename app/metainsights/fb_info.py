# pylint: disable=no-member
"""Gets Info For various Meta Accounts"""

import logging
import requests

from .models import FacebookPage


# Create Functions here.
def get_facebook_pages(access_token):
    """Gets Facebook Pages for a given access token"""
    url = "https://graph.facebook.com/v20.0/me/accounts"

    try:
        response = requests.get(url, params={'access_token': access_token}, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error('HTTP error occurred: %s', http_err)
        return None

def ig_account_info(access_token, page_id):
    """Gets Instagram Account Info for a given access token and page id"""
    url = f"https://graph.facebook.com/v20.0/{page_id}"
    params={
        "fields": "instagram_business_account",
        'access_token': access_token
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error('HTTP error occurred: %s', http_err)
        return None

def get_page_id_by_cli_name(cli_name):
    """Gets Page ID by Client Name"""
    try:
        page = FacebookPage.objects.get(cli_name=cli_name)
        return page.page_id
    except FacebookPage.DoesNotExist:
        logging.error("No FacebookPage found with cli_name: %s", cli_name)
    return None

def update_ig_user_id(cli_name, ig_user_id):
    """Updates Instagram User ID for a given Client Name"""
    try:
        page = FacebookPage.objects.get(cli_name=cli_name)
        page.ig_user_id = ig_user_id
        page.save()
        logging.info("Successfully updated %s FacebookPage model!", cli_name)
    except FacebookPage.DoesNotExist:
        logging.error("No FacebookPage found with cli_name: %s", cli_name)

def get_ig_user_id_by_cli_name(cli_name):
    """Gets Instagram User ID by Client Name"""
    try:
        page = FacebookPage.objects.get(cli_name=cli_name)
        return page.ig_user_id
    except FacebookPage.DoesNotExist:
        logging.error("No FacebookPage found with cli_name: %s", cli_name)
    return None
