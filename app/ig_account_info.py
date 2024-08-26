"""Grabs IG Account Info."""

import argparse
import logging
import os

import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vonfitbjjInsights.settings')
django.setup()

# pylint: disable=wrong-import-position
# ruff: noqa: E402
from metainsights.fb_info import (
    get_page_id_by_cli_name,
    ig_account_info,
    update_ig_user_id,
)
from metainsights.fb_utils import get_latest_access_token
from metainsights.setup_env import setup_django_environment
from metainsights.setup_env import setup_logging
from metainsights.error_handlers import ArgumentErrors

# Set up Django environment and logging
setup_django_environment()
logger = setup_logging()

# Call Function
if __name__ == "__main__":
    with ArgumentErrors():
        parser = argparse.ArgumentParser(description='Fetch Instagram account info.')
        parser.add_argument('cli_name', type=str, help='CLI friendly name of the Facebook page')

        args = parser.parse_args()
        name = args.cli_name

        page_id = get_page_id_by_cli_name(name)
        if page_id:
            access_token = get_latest_access_token()
            if access_token:
                info = ig_account_info(access_token, page_id)
                if info and 'instagram_business_account' in info:
                    ig_user_id = info['instagram_business_account']['id']
                    update_ig_user_id(name, ig_user_id)
                    logging.info('IG Account ID %s added to %s', ig_user_id, name)
                else:
                    logging.error("Failed to retrieve Instagram account info.")
            else:
                logging.error("Failed to retrieve access token.")
        else:
            logging.error("Failed to find the page ID for the provided CLI name.")
