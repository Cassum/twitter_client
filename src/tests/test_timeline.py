from twit_cli.timeline import Timeline


def test_it_stores_tweets():
    timeline = Timeline(['foo', 'bar'])
    assert timeline.tweets == ['foo', 'bar']
