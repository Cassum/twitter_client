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
            Default.name: curses.A_NORMAL,
            Black.name: 0,
            Red.name: curses.color_pair(1),
            Green.name: curses.color_pair(2),
            Yellow.name: curses.color_pair(3),
            Blue.name: curses.color_pair(4),
            Cyan.name: curses.color_pair(5),
            Magenta.name: curses.color_pair(6),
            White.name: curses.color_pair(7),
        }

    def init_ui(self):
        self.screen = curses.initscr()
        curses.start_color()
        curses.noecho()
        curses.use_default_colors()
        self.screen.scrollok(True)
        self.screen.idlok(True)
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
            color = self.color_pairs[item.color.name]
            for mod in item.color.modificators:
                color |= mod
            self.screen.addstr(item.text, color)

    def clear(self):
        self.screen.erase()
        self.refresh()

    @property
    def max_width(self):
        return self.screen.getmaxyx()[1] - 1
