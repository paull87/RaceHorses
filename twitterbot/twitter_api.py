#!/usr/bin/python3

import tweepy

class TwitterAPI:
    """Class for the authentication of twitter api."""

    def __init__(self):
        """Initialise the twitter api."""
        self.api = authenticate_twitter()


def authenticate_twitter():
    """Authenticates the twitter API from the given tokens."""
    consumer_key = ''
    consumer_secret = ''
    access_key = ''
    access_secret = ''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    try:
        return tweepy.API(auth)
    except Exception as e:
        raise 'Unable to authenticate twitter API: {}'.format(e)

