import curses


class CursesUI:
    def __init__(self):
        self.screen = None

    def init_ui(self):
        self.screen = curses.initscr()
        curses.init_color()

    def refresh(self):
        self.screen.refresh()
    
    def teardown(self):
        curses.endwin()
