import requests
import logging

# Create Functions here.
def ig_audience_dem(
        access_token,
        ig_user_id,
        metric
    ):
    url = f"https://graph.facebook.com/v17.0/{ig_user_id}/insights"
    params={
        'metric': metric,
        'period': 'lifetime',
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