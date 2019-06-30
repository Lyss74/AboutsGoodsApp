"""
    This file has the responsibility to offer the possibility of
    being able to add in an independent table the favorite
    characters to be able to find them more easily
"""
from django.core.management.base import BaseCommand, CommandError

import requests as req

from app.models import Episode


class Command(BaseCommand):
    help = 'Download all episodes'

    def handle(self, *args, **options):
        """

        """
        pass


# python manage.py commands.file