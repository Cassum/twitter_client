from twit_cli.tweet import Tweet


def test_it_has_text_and_author():
    tweet = Tweet('gary', 'some text')
    assert tweet.author == 'gary'
    assert tweet.text == 'some text'
