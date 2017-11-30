import curses

from twit_cli.curses_tweet_renderer import CursesTweetRenderer
from twit_cli.tweet import Tweet
from twit_cli.text import Text, Green, Default


def test_it_renders_single_line_tweets():
    tweet = Tweet(
        'fooser',
        'this is a tweet',
    )

    expected = Text(
        '         ',
        Green(),
        'fooser',
        Default(),
        ' ',
        'this is a tweet',
    )
    assert expected == CursesTweetRenderer.render(tweet)


def test_it_renders_multiline_tweets():
    tweet = Tweet(
        'fooser',
        'this is a tweet\nwith two lines',
    )

    expected = Text(
        '         ',
        Green(),
        'fooser',
        Default(),
        ' ',
        'this is a tweet',
        '\n                with two lines',
    )
    assert expected == CursesTweetRenderer.render(tweet)


def test_it_underlines_selected_tweets():
    tweet = Tweet(
        'fooser',
        'this is a tweet',
    )

    expected = Text(
        '         ',
        Green(),
        'fooser',
        Default([curses.A_UNDERLINE]),
        ' ',
        'this is a tweet',
    )
    assert expected == CursesTweetRenderer.render(tweet, True)
