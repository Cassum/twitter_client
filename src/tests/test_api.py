from unittest import mock

import twitter

from twit_cli.api import API


def test_it_fetches_timeline():
    with mock.patch('twitter.Api') as tw_api:
        api = API()
        timeline = mock.MagicMock()
        tw_api().GetHomeTimeline.return_value = timeline
        assert api.get_timeline(100) == timeline
        tw_api().GetHomeTimeline.assert_called_once_with(100)


def test_it_initializes_properly():
    with mock.patch('twitter.Api') as tw_api:
        api = API(
            consumer_key='consumer_key',
            consumer_secret='consumer_secret',
            access_token_key='access_token_key',
            access_token_secret='access_token_secret',
        )
        tw_api.assert_called_once_with(
            consumer_key='consumer_key',
            consumer_secret='consumer_secret',
            access_token_key='access_token_key',
            access_token_secret='access_token_secret',
        )
