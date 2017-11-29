import curses

from twit_cli.text import (
    Default,
    Black,
    Red,
    Green,
    Yellow,
    Blue,
    Cyan,
    Magenta,
    White,
)


class CursesUI:
    def __init__(self):
        self.screen = None
        self.color_pairs = {}

    def _init_color_pairs(self):
        curses.init_pair(1, curses.COLOR_RED, -1)
        curses.init_pair(2, curses.COLOR_GREEN, -1)
        curses.init_pair(3, curses.COLOR_YELLOW, -1)
        curses.init_pair(4, curses.COLOR_BLUE, -1),
        curses.init_pair(5, curses.COLOR_CYAN, -1),
        curses.init_pair(6, curses.COLOR_MAGENTA, -1),
        curses.init_pair(7, curses.COLOR_WHITE, -1),
        self.color_pairs = {
            Default: curses.A_NORMAL,
            Black: 0,
            Red: curses.color_pair(1),
            Green: curses.color_pair(2),
            Yellow: curses.color_pair(3),
            Blue: curses.color_pair(4),
            Cyan: curses.color_pair(5),
            Magenta: curses.color_pair(6),
            White: curses.color_pair(7),
        }

    def init_ui(self):
        self.screen = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.use_default_colors()
        self._init_color_pairs()
        self.refresh()

    def refresh(self):
        self.screen.refresh()

    def teardown(self):
        curses.endwin()

    def __enter__(self):
        self.init_ui()
        return self

    def __exit__(self, *args):
        self.teardown()

    def loop(self):
        while True:
            ch = self.screen.getch()
            self.refresh()
            yield ch

    def print(self, string):
        self.screen.addstr(string + '\n')
        self.refresh()

    def print_text(self, text):
        for item in text:
            self.screen.addstr(item.text, self.color_pairs[item.color])
        self.screen.addstr('\n')
        self.refresh()


    def clear(self):
        self.screen.erase()
        self.refresh()
