#!/usr/bin/env python
import os

import yaml

from twit_cli.api import API
from twit_cli.ui import CursesUI
from twit_cli.tweet import Tweet
from twit_cli.curses_tweet_renderer import CursesTweetRenderer


if __name__ == '__main__':
    credentials = yaml.load(open(
        os.path.join(
            os.path.dirname(__file__),
            'creds.yaml',
        ),
    ))
    api = API(
        consumer_key=credentials['consumer_key'],
        consumer_secret=credentials['consumer_secret'],
        access_token_key=credentials['access_token_key'],
        access_token_secret=credentials['access_token_secret'],
    )
    with CursesUI() as ui:
        for tw in reversed(api.get_timeline(20)):
            tweet = Tweet(tw.user.screen_name, tw.text)
            ui.print_text(CursesTweetRenderer.render(tweet))
        for ch in ui.loop():
            if ord('q') == ch:
                break
