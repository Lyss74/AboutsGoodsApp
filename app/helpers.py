import requests

class RickAndMortyAPI:
    """Class abstracting Rick&Morty API to get info about characters, episodes
    and locations.

    Attributes:
    ==========
        base_url (str): base url for Rick & Morty REST API

    """

    def __init__(self):
        self.base_url = "https://rickandmortyapi.com/api/"

    @property
    def characters(self):
        """List of dictionaries representing characters from Rick & Morty."""
        self.step('Characters[...]')
        print("L'insertions dans la base de donnèes va débuter")
        return self._fetch(self.base_url + "character/")

    @property
    def episodes(self):
        """List of dictionaries representing episodes from Rick & Morty."""
        self.step('Episodes[...]')
        print("L'insertions dans la base de donnèes va débuter")
        return self._fetch(self.base_url + "episode/")

    @property
    def locations(self):
        """List of dictionaries representing locations from Rick & Morty."""
        self.step('Locations[...]')
        print("L'insertions dans la base de donnèes va débuter")
        return self._fetch(self.base_url + "location/")

    def _fetch(self, url):
        """Fetches entries from several pages from REST API and returns them 
        in a single list.
        """
        entries = []
        while url:
            data = requests.get(url).json()
            entries.extend(data['results'])
            url = data['info']['next']
        return entries

    def step(self, name):
        print(f"The download: {name} successful")
