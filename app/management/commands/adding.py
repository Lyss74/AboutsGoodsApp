"""
    This file has the responsibility of being able
    to add a planet or a character relative to the series.
"""
from django.core.management.base import BaseCommand, CommandError

import requests as req

from pprint import pprint

from app.models import Character
