"""Sets Up Environment"""

import os
import logging
import django

def setup_django_environment(settings_module='vonfitbjjInsights.settings'):
    """Sets up the Django environment."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    django.setup()

def setup_logging(level=logging.INFO):
    """Sets up logging configuration."""
    logger = logging.getLogger('metainsights')
    logging.basicConfig(level=level, format='%(message)s')
    return logger
