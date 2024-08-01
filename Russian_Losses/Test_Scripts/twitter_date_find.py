import re
from datetime import datetime, timedelta

# Function to extract tweet ID from URL
def extract_tweet_id(url):
    match = re.search(r'/status/(\d+)', url)
    if match:
        return int(match.group(1))
    return None

# Function to convert tweet ID to timestamp
def get_tweet_time(tweet_id):
    twitter_epoch = 1288834974657  # Twitter epoch time in milliseconds
    tweet_timestamp = (tweet_id >> 22) + twitter_epoch
    tweet_datetime = datetime.utcfromtimestamp(tweet_timestamp / 1000.0)
    return tweet_datetime

# Main script to check individual Twitter URLs
def main():
    while True:
        tweet_url = input("Enter Twitter URL (or 'exit' to quit): ").strip()
        if tweet_url.lower() == 'exit':
            break
        tweet_id = extract_tweet_id(tweet_url)
        if not tweet_id:
            print("Invalid Twitter URL")
            continue
        tweet_time = get_tweet_time(tweet_id)
        print(f"Tweet Date and Time (UTC): {tweet_time}")

if __name__ == "__main__":
    main()
