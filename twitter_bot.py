from DownloadHorses import Horses
import tweepy, time, sys

# enter the corresponding information from your Twitter application:
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

from_user = '@plucas87'

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

print(message)

api.send_direct_message(user='plucas87', text=message)
