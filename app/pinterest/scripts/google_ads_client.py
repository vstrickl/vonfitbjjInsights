"""This module sets up your Google Ads Client"""
import json
from django.conf import settings
import google.auth
from google.ads.google_ads.client import GoogleAdsClient

# Load credentials
CREDS = settings.BLOG_POSTS_JSON
with open(CREDS, encoding="utf-8") as f:
    credentials = json.load(f)

client_id = credentials["client_id"]
client_secret = credentials["client_secret"]

# Authenticate Google Ads API Client
client = GoogleAdsClient.load_from_storage("google-ads.yaml")
