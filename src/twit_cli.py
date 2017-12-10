#!/usr/bin/env python
import os
import curses
import threading
import time

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


def get_timeline(api):
    return Timeline(
        list(reversed(list(
            Tweet(tw.user.screen_name, tw.text, tw.id)
            for tw in api.get_timeline(100)
          )))
    )


def find_cursor_position(old_cur, new_timeline):
    id = old_cur.current.id
    for i, tw in enumerate(new_timeline.tweets):
        if tw.id == id:
            return i
    return len(new_timeline.tweets) - 1


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
    timeline = get_timeline(api)
    with CursesUI() as ui:
        cursor = Cursor(timeline.tweets, len(timeline.tweets) - 1)
        redraw(ui, timeline.tweets, cursor)
        for ch in ui.loop():
            if ord('q') == ch:
                break
            elif ch in [ord('j'), curses.KEY_DOWN, 66]:
                cursor = cursor.down()
            elif ch in [ord('k'), curses.KEY_UP, 65]:
                cursor = cursor.up()
            elif ch == ord('r'):
                timeline = get_timeline(api)
                cur_pos = find_cursor_position(cursor, timeline)
                cursor = Cursor(timeline.tweets, cur_pos)
            redraw(ui, timeline.tweets, cursor)
