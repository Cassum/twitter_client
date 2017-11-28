class TweetRenderer:
    @staticmethod
    def render(tweet):
        lines = tweet.text.splitlines()
        result = '{:>15} {}'.format(tweet.author, lines[0])
        for line in lines[1:]:
            result += '\n' + ' '*16 + line
        return result
