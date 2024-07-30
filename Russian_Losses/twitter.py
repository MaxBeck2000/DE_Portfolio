import re
from datetime import datetime

def extract_tweet_id(url):
    match = re.search(r'/status/(\d+)', url)
    if match:
        return int(match.group(1))
    return None

def get_tweet_time(tweet_id):
    if tweet_id is None:
        return None
    twitter_epoch = 1288834974657  # Twitter epoch time in milliseconds
    tweet_timestamp = (tweet_id >> 22) + twitter_epoch
    tweet_datetime = datetime.utcfromtimestamp(tweet_timestamp / 1000.0)
    return tweet_datetime
