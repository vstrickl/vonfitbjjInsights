import requests
import logging

# Create Functions here.
def ig_audience_dem(
        access_token,
        ig_user_id,
        metric,
        timeframe=None,
        metric_type=None,
        breakdown=None,
        since=None,
        until=None
    ):
    api_version = 17.0
    url = f"https://graph.facebook.com/v{api_version}/{ig_user_id}/insights"
    params={
        'metric': metric,
        'period': 'lifetime',
        'access_token': access_token
    }

    if since and until:
        params['since'] = since
        params['until'] = until

    if metric == 'engaged_audience_demographics':
        if timeframe:
            params['timeframe'] = timeframe
        if metric_type:
            params['metric_type'] = metric_type
        if breakdown:
            params['breakdown'] = breakdown

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        logging.error(f'HTTP error occurred: {http_err}')
    except Exception as err:
        logging.error(f'An error occurred: {err}')