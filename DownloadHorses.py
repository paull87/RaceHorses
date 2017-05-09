#!/usr/bin/python3

import requests
import bs4
from Horse import Horse


class Horses:
    """Class containing horses running for the day."""

    def __init__(self, site):
        """Initialise the trainer prices"""
        self.site = site
        self.horses = []
        self._get_horses()

    def _get_horses(self):
        """Gets the details for each horse found."""
        soup = download_page(self.site)
        items = get_items(soup)
        for item in items:
            horse = find_horse(item)
            if horse:
                self.horses.append(horse)

    def show_horses(self, searches):
        """Checks to see if horses have any of the given names."""
        for horse in self.horses:
            for search in searches:
                if search.lower() in horse.name.lower():
                    horse.display_horse()
                    break

    def search_horses(self, searches):
        """Checks to see if horses have any of the given names."""
        output = ''
        for horse in self.horses:
            for search in searches:
                if search.lower() in horse.name.lower():
                    output += horse.horse_format() + '\n\n'
                    break
        return output

def download_page(site):
    """Downloads and parses the website, returning the bs4 result."""
    res = requests.get(site)
    with open('C://temp//RacehorseDB.txt', 'w') as text_file:
        text_file.write(res.text)
    try:
        return bs4.BeautifulSoup(res.text, 'html.parser')
    except Exception as e:
        raise 'Unable to parse website due to {}'.format(e)


def get_items(soup):
    """Takes parsed html and returns all horse elements."""
    try:
        return soup.find_all(class_='databreakdown18')
    except Exception as e:
        raise "Unable to find any items: {}".format(e)


def find_horse(item):
    """Finds horse details in the given html element."""
    details = [x for x in item.contents if x != '\n']
    try:
        return Horse(details[0].text, details[1].text, details[2].text,
                     details[5].text, details[7].text)
    except Exception as e:
        raise 'Unable to determine horse details due to {}'.format(e)

if __name__ == '__main__':

    url = 'http://www.horseracebase.com/atoz.php'
    my_horses = Horses(url)

    #for horse in my_horses.horses:
    #    horse.display_horse()

    print(my_horses.search_horses(['Poppy', 'Pop', 'October', 'Gem', 'World']))
