import os
import django
import logging
import argparse

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vonfitbjjInsights.settings')
django.setup()

from metainsights.fb_info import ig_account_info
from metainsights.fb_info import get_page_id_by_cli_name
from metainsights.fb_info import update_ig_user_id
from metainsights.fb_utils import get_latest_access_token

# Set up logging
logger = logging.getLogger('metainsights')
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Call Function
if __name__ == "__main__":
    try:
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
                    logging.info(f'IG Account ID {ig_user_id} added to {name}')
                else:
                    logging.error("Failed to retrieve Instagram account info.")
            else:
                logging.error("Failed to retrieve access token.")
        else:
            logging.error("Failed to find the page ID for the provided CLI name.")
    except argparse.ArgumentError as arg_err:
        logging.error(f'Argument error: {arg_err}')
    except django.core.exceptions.ImproperlyConfigured as config_err:
        logging.error(f'Improperly configured: {config_err}')
    except django.db.utils.DatabaseError as db_err:
        logging.error(f'Database error: {db_err}')
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")