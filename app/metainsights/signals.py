"""Captures the Facebook Access Token when the User Logs in."""
import logging
from allauth.socialaccount.models import SocialToken
from allauth.socialaccount.signals import social_account_added
from django.dispatch import receiver

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@receiver(social_account_added)
def social_account_added_callback(request, sociallogin, **kwargs):
    if sociallogin.account.provider == 'facebook':
        token = SocialToken.objects.get(account=sociallogin.account).token
        # You can now use the token to make API requests
        logger.info(f"Access token: {token}")
        # Optionally, save the token to the user's profile or another model
