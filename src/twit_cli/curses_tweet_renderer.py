from twit_cli.text import Text, Green, Default


class CursesTweetRenderer:
    @staticmethod
    def render(tweet):
        lines = tweet.text.splitlines()
        spacing = ' ' * (15 - len(tweet.author))
        result = Text(
            spacing,
            Green,
            tweet.author,
            Default,
            ' ',
            lines[0],
        )
        for line in lines[1:]:
            result += Text('\n' + ' '*16 + line)
        return result
