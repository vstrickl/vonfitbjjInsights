"""Handles Common Error Messages"""

import logging
import argparse
import django

class ArgumentErrors:
    """Handles Argument Errors"""
    def __enter__(self):
        # You can initialize anything here if needed
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            if issubclass(exc_type, argparse.ArgumentError):
                logging.error('Argument error: %s', exc_value)
                return True  # Suppress the exception
            elif issubclass(exc_type, django.core.exceptions.ImproperlyConfigured):
                logging.error('Improperly configured: %s', exc_value)
                return True  # Suppress the exception
            elif issubclass(exc_type, django.db.utils.DatabaseError):
                logging.error('Database error: %s', exc_value)
                return True  # Suppress the exception
        return False  # Do not suppress other exceptions