import os
import json
import django
import logging
import argparse

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vonfitbjjInsights.settings')
django.setup()

from metainsights.fb_utils import get_latest_access_token
from metainsights.fb_info import get_ig_user_id_by_cli_name
from metainsights.insights import ig_audience_dem

# Set up logging
logger = logging.getLogger('metainsights')
logging.basicConfig(level=logging.INFO, format='%(message)s')

# Call Function
if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Fetch Instagram audience demographics.')
        parser.add_argument('cli_name', type=str, help='CLI name of the Facebook page')
        parser.add_argument('metric', type=str, help='Metric to fetch')
        parser.add_argument('--since', type=str, help='Start date for the data', required=False)
        parser.add_argument('--until', type=str, help='End date for the data', required=False)
        parser.add_argument('--timeframe', type=str, help='Timeframe for engaged_audience_demographics', required=False)
        parser.add_argument('--metric_type', type=str, help='Metric type for engaged_audience_demographics', required=False)
        parser.add_argument('--breakdown', type=str, help='Breakdown for engaged_audience_demographics', required=False)

        args = parser.parse_args()

        ig_user_id = get_ig_user_id_by_cli_name(args.cli_name)
        if ig_user_id:
            access_token = get_latest_access_token()
            if access_token:
                result = ig_audience_dem(
                    access_token,
                    ig_user_id,
                    args.metric,
                    args.since,
                    args.until,
                    args.timeframe,
                    args.metric_type,
                    args.breakdown
                )
                if result:
                    logging.info(f'\nSuccessfully retrieved {args.metric} IG Insights...\n')
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
    except argparse.ArgumentError as arg_err:
        logging.error(f'Argument error: {arg_err}')
    except django.core.exceptions.ImproperlyConfigured as config_err:
        logging.error(f'Improperly configured: {config_err}')
    except django.db.utils.DatabaseError as db_err:
        logging.error(f'Database error: {db_err}')
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")