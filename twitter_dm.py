#!/usr/bin/python3

from DownloadHorses import Horses
from twitter_api import TwitterAPI


def get_horses(searches):
    """Finds today's horses."""
    todays_horses = Horses('http://www.horseracebase.com/atoz.php')
    return todays_horses.search_horses(searches)


def send_dm(handle, text):
    """Sends the given messaage as a dm to the given user."""
    twitter = TwitterAPI()
    try:
        twitter.api.send_direct_message(user=handle, text=text)
    except Exception as e:
        raise 'Unable to send dm: {}'.format(e)


def create_message(items):
    """creates message depending on content of given text"""
    if items != '':
        return "These are today's horses -\n\n" + items
    else:
        return "There are no horses running today that meet your searches."


if __name__ == '__main__':

    # User to send the dm to
    user = 'plucas87'

    # Key words to search horse names for
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

    # Find today's horses
    horses = get_horses(key_words)
    
    # Send the dm message
    send_dm(user, create_message(horses))
