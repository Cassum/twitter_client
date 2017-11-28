from twit_cli.tweet_renderer import TweetRenderer
from twit_cli.tweet import Tweet


def test_it_renders_single_line_tweets():
    tweet = Tweet(
        'fooser',
        'this is a tweet',
    )

    expected = '         fooser this is a tweet'
    assert expected == TweetRenderer.render(tweet)


def test_it_renders_multiline_tweets():
    tweet = Tweet(
        'fooser',
        'this is a tweet\nwith two lines',
    )

    expected = (
        '         fooser this is a tweet\n'
        '                with two lines'
    )
    assert expected == TweetRenderer.render(tweet)
