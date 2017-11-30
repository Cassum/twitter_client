import curses

from twit_cli.text import Text, Green, Default


class CursesTweetRenderer:
    @staticmethod
    def render(tweet, selected=False):
        lines = tweet.text.splitlines()
        spacing = ' ' * (15 - len(tweet.author))
        if selected:
            modificators = [curses.A_UNDERLINE]
        else:
            modificators = []
        result = Text(
            spacing,
            Green(),
            tweet.author,
            Default(modificators),
            ' ',
            lines[0],
        )
        for line in lines[1:]:
            result += Text('\n' + ' '*16 + line)
        return result
