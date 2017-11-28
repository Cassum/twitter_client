#!/usr/bin/env python
import yaml

from twit_cli.api import API
from twit_cli.tweet import Tweet
from twit_cli.tweet_renderer import TweetRenderer


if __name__ == '__main__':
    credentials = yaml.load(open('creds.yaml'))
    api = API(
        consumer_key=credentials['consumer_key'],
        consumer_secret=credentials['consumer_secret'],
        access_token_key=credentials['access_token_key'],
        access_token_secret=credentials['access_token_secret'],
    )
    for tw in reversed(api.get_timeline(20)):
        tweet = Tweet(tw.user.screen_name, tw.text)
        print(TweetRenderer.render(tweet))
