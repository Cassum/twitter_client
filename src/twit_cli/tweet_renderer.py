from termcolor import colored


class TweetRenderer:
    @staticmethod
    def render(tweet):
        lines = tweet.text.splitlines()
        spacing = ' ' * (15 - len(tweet.author))
        result = '{}{} {}'.format(
            spacing,
            colored(tweet.author, 'green'),
            lines[0],
        )
        for line in lines[1:]:
            result += '\n' + ' '*16 + line
        return result
