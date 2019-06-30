"""
    This file is responsible for collecting all data related to the characters in the series
"""
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError

from app.helpers import RickAndMortyAPI
from app.models import Character, Episode, Location


class Command(BaseCommand):
    help = 'Update the database content'

    def handle(self, *args, **kwarg):
        """Command entry point."""
        self.data = RickAndMortyAPI()
        self._save_locations()
        self._save_episodes()
        self._save_characters()

    def _save_locations(self):
        """Saves locations in the database."""
        Location.objects.all().delete()
        self.locations = {}
        for location in self.data.locations:
            self.locations[location['url']] = Location.objects.create(
                id=location['id'],
                name=location['name'],
                location_type=location['type'],
                dimension=location['dimension'],
                url=location['url'],
                created=location['created']
            )
            self.step('Locations[...]')

    def _save_episodes(self):
        """Saves episodes in the database."""
        Episode.objects.all().delete()
        self.episodes = {}
        for episode in self.data.episodes:
            self.episodes[episode['url']] = Episode.objects.create(
                id=episode['id'],
                name=episode['name'],
                air_date=episode['air_date'],
                episode=episode['episode'],
                url=episode['url'],
                created=episode['created']
            )
            self.step('Episodes[...]')

    def _save_characters(self):
        """Saves characters in the database."""
        Character.objects.all().delete()
        for character in self.data.characters:
            c = Character.objects.create(
                id=character['id'],
                name=character['name'],
                status=character['status'],
                species=character['species'],
                character_type=character['type'],
                gender=character['gender'],
                origin=self.locations.get(character['origin']['url']),
                location=self.locations.get(character['origin']['url']),
                image_url=character['image'],
                url=character['url'],
                created=character['created']
            )
            c.episodes.add(*[self.episodes[url] for url in character['episode']])
            self.step('Characters.')
            print('Vous pouvez lancer le serveur Django.')

    def step(self, name):
        print(f"The insert data {name} successful")
