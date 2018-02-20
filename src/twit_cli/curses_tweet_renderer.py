import curses

from twit_cli.text import Text, Green, Default, Blue


# TODO: extract all math into reasonable representation
class CursesTweetRenderer:
    @staticmethod
    def split_for_max_width(line, max_width, modificators):
        if max_width is None:
            return [Text(Default(modificators), line)]
        max_width -= 16  # spacing + '> '
        result = []
        remains = line
        first_part_of_line = True
        while remains:
            if first_part_of_line:
                screen_line, remains = (
                    Text(Default(modificators), remains[:max_width]),
                    remains[max_width:],
                )
                first_part_of_line = False
            else:
                screen_line, remains = (
                    Text(
                        Blue(),
                        '| ',
                        Default(modificators),
                        remains[:max_width-2],
                    ),
                    remains[max_width-2:],
                )
            result.append(screen_line)
        return result

    @staticmethod
    def render(tweet, selected=False, max_width=None):
        lines = tweet.text.splitlines()
        spacing = ' ' * (15 - len(tweet.author))
        if selected:
            modificators = [curses.A_UNDERLINE]
        else:
            modificators = []
        first_line = True
        result = Text()
        for line in lines:
            splitted_line = CursesTweetRenderer.split_for_max_width(
                line,
                max_width,
                modificators,
            )
            for screen_line in splitted_line:
                # raise RuntimeError(splitted_line)
                if first_line:
                    result += Text(
                        spacing,
                        Green(),
                        tweet.author,
                        Default(),
                        ' ',
                        Default(modificators),
                    ) + screen_line
                    first_line = False
                else:
                    result += Text(
                        Default(),
                        '\n' + ' '*16,
                    ) + screen_line
        result += Text(Default(), '\n')
        return result
