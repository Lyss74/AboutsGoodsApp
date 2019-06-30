"""
    This file structure the database:
    1.Launch the make migration in terminal
        'python manage.py makemigrations'
    2.Launch the migrates for all table in application
        'python manage.py migrate'
    3.You can now consult your database in the
      '0001_initial.py' file in the 'migrations' folder
"""
from django.db import models
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation
)
from django.contrib.contenttypes.models import ContentType


class Character(models.Model):
    """ Creating the structure the table "Character" for database """
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    species = models.CharField(max_length=255, blank=True, null=True)
    character_type = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    origin = models.ForeignKey('Location', on_delete=models.CASCADE, null=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE,
                                 related_name='characters', null=True)
    image_url = models.URLField(blank=True, null=True)
    episodes = models.ManyToManyField('Episode', related_name='characters')
    url = models.URLField(blank=True, null=True)
    favorite = GenericRelation('Favorite', related_query_name='character')
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Converted the attribute object to string objects"""
        return self.name


class Location(models.Model):
    """
        Creating the structure the table "Location" for database
    """
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    location_type = models.CharField(max_length=255, blank=True, null=True)
    dimension = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    favorite = GenericRelation('Favorite', related_query_name='location')
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Converted the attribute object to string objects"""
        return self.name


class Episode(models.Model):
    """
        Creating the structure the table "Episodes" for database
    """
    # episode_id = The id is auto generate by
    # SQLite associated with a pimaire key
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    air_date = models.CharField(max_length=255, blank=True, null=True)
    episode = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    favorite = GenericRelation('Favorite', related_query_name='episode')
    created = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Converted the attribute object to string objects"""
        return self.name


class Favorite(models.Model):
    """
        Creation of the table "Favorites", to store the
        preferred residents with their rental and type
    """
    favorite_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    favorite_id = models.PositiveIntegerField()
    favorite = GenericForeignKey('favorite_type', 'favorite_id')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.favorite_type}{self.favorite.name}"

    def __str__(self):
        """ Converted the attribute object to string objects"""
        return self.resident
