import curses

from twit_cli.curses_tweet_renderer import CursesTweetRenderer
from twit_cli.tweet import Tweet
from twit_cli.text import Text, Green, Default, Blue


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
        '\n',
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
        '\n                ',
        'with two lines',
        '\n',
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
        Default(),
        ' ',
        Default([curses.A_UNDERLINE]),
        'this is a tweet',
        Default(),
        '\n',
    )
    assert expected == CursesTweetRenderer.render(tweet, selected=True)


def test_it_underlines_selected_tweets_for_multiline_tweets():
    tweet = Tweet(
        'fooser',
        'this is a\nmultiline tweet',
    )

    expected = Text(
        '         ',
        Green(),
        'fooser',
        Default(),
        ' ',
        Default([curses.A_UNDERLINE]),
        'this is a',
        Default(),
        '\n                ',
        Default([curses.A_UNDERLINE]),
        'multiline tweet',
        Default(),
        '\n',
    )
    assert expected == CursesTweetRenderer.render(tweet, selected=True)


def test_renders_with_limited_screen_width():
    tweet_text = (
        'This is a long tweet, its 68 characters long. ZzZzZzZzZzZzZzZzZzZzZz'
    )
    assert 68 == len(tweet_text)
    tweet = Tweet(
        'fooser',
        tweet_text,
    )
    expected = Text(
        '         ',
        Green(),
        'fooser',
        Default(),
        ' ',
        'This is a long tweet, its 68 characters long. ',
        '\n                ',
        Blue(),
        '| ',
        Default(),
        'ZzZzZzZzZzZzZzZzZzZzZz',
        '\n',
    )
    assert expected == CursesTweetRenderer.render(tweet, max_width=62)
