#!/usr/bin/python3

from DownloadHorses import Horses
from twitter_api import TwitterAPI

twitter = TwitterAPI()

todays_horses = Horses('http://www.horseracebase.com/atoz.php')

key_words = [
    'Poppy',
    'Pop',
    'October',
    'Gem',
    'Gemma',
    'Lucas',
    'June',
    'Spring Vale',
    'Reverdy',
    'Garner',
]

my_horses = todays_horses.search_horses(key_words)
message = "These are today's horses -\n\n" + my_horses

try:
    twitter.api.send_direct_message(user='plucas87', text=message)
except Exception as e:
    raise 'Unable to send dm: {}'.format(e)