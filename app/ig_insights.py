"""Calls the IG Insights API Endpoint function."""

import argparse
import json
import logging
import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vonfitbjjInsights.settings')
django.setup()

# pylint: disable=wrong-import-position
# ruff: noqa: E402
from metainsights.fb_info import get_ig_user_id_by_cli_name
from metainsights.fb_utils import get_latest_access_token
from metainsights.insights import ig_audience_dem
from metainsights.error_handlers import ArgumentErrors

# Set up logging
logger = logging.getLogger('metainsights')
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Call Function
if __name__ == "__main__":
    with ArgumentErrors():
        parser = argparse.ArgumentParser(description='Fetch Instagram audience demographics.')
        parser.add_argument('cli_name', type=str, help='CLI friendly name of the Facebook page')
        parser.add_argument('metric', type=str, help='Metric to fetch')

        args = parser.parse_args()

        ig_user_id = get_ig_user_id_by_cli_name(args.cli_name)
        if ig_user_id:
            access_token = get_latest_access_token()
            if access_token:
                result = ig_audience_dem(
                    access_token,
                    ig_user_id,
                    args.metric,
                )
                if result:
                    logging.info('\nSuccessfully retrieved %s IG Insights...\n', args.metric)
                    for data in result.get('data', []):
                        if 'values' in data:
                            for value in data['values']:
                                formatted_value = json.dumps(value['value'], indent=4)
                                logging.info(formatted_value)
                else:
                    logging.error("Failed to retrieve Instagram audience demographics.")
            else:
                logging.error("Failed to retrieve access token.")
        else:
            logging.error("Failed to find the IG user ID for the provided CLI name.")
