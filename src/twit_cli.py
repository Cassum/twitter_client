#!/usr/bin/env python
import os

import yaml

from twit_cli.api import API
from twit_cli.curses_tweet_renderer import CursesTweetRenderer
from twit_cli.cursor import Cursor
from twit_cli.timeline import Timeline
from twit_cli.tweet import Tweet
from twit_cli.ui import CursesUI


def redraw(ui, tweets, cursor):
    ui.clear()
    for tweet in tweets:
        ui.print_text(
            CursesTweetRenderer.render(
                tweet,
                cursor.current is tweet,
            ),
        )
    ui.refresh()


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
    timeline = Timeline(
        list(reversed(list(
            Tweet(tw.user.screen_name, tw.text)
            for tw in api.get_timeline(100)
          )))
    )
    with CursesUI() as ui:
        cursor = Cursor(timeline.tweets, len(timeline.tweets) - 1)
        redraw(ui, timeline.tweets, cursor)
        for ch in ui.loop():
            if ord('q') == ch:
                break
            elif ord('j') == ch:
                cursor = cursor.down()
            elif ord('k') == ch:
                cursor = cursor.up()
            redraw(ui, timeline.tweets, cursor)
