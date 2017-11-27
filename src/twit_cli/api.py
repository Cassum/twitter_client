import twitter


class API:
    def __init__(self, **kwargs):
        self._api = twitter.Api(**kwargs)

    def get_timeline(self, count=None):
        return self._api.GetHomeTimeline(count)
