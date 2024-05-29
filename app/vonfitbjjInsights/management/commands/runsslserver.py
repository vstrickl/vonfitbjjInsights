"""Enables an SSL development server for the project."""

from django.core.management.base import BaseCommand
from django.core.management import call_command
from pathlib import Path

class Command(BaseCommand):
    help = 'Runs the Django SSL server with specified certificate and key'

    def handle(self, *args, **options):
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        certificate = base_dir / 'django.crt'
        key = base_dir / 'django.key'

        call_command('runsslserver', '--certificate', str(certificate), '--key', str(key))