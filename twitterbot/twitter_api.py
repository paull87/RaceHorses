#!/usr/bin/python3


import tweepy
import json


class TwitterAPI:
    """Class for the authentication of twitter api."""

    def __init__(self):
        """Initialise the twitter api."""
        self.api = self.authenticate_twitter()
        self.keys = get_keys()

    def key(self, key_name):
        """Returns the key value for the given key name."""
        try:
            return self.keys[key_name]
        except KeyError as e:
            raise 'No key found for {}'.format(key_name)

    def authenticate_twitter(self):
        """Authenticates the twitter API from the given tokens."""
        consumer_key = self.key['consumer_key']
        consumer_secret = self.key['consumer_secret']
        access_key = self.key['access_key']
        access_secret = self.key['access_secret']
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_key, access_secret)
        try:
            return tweepy.API(auth)
        except Exception as e:
            raise 'Unable to authenticate twitter API: {}'.format(e)


def get_keys():
    """Gets the keys from the json file."""
    try:
        with open('keys.json') as key_file:
            return json.loads(key_file.read())
    except Exception as e:
        raise 'Unable to open json file: {}'.format(e)


def key(key_name, keys=keys):
    """Returns the key value for the given key name."""
    try:
        return keys[key_name]
    except KeyError as e:
        raise 'No key found for {}'.format(key_name)

