class Cursor:
    def __init__(self, items, index):
        self.items = items
        self.index = index

    def down(self):
        return Cursor(self.items, self.index + 1) \
            if self.index < (len(self.items) - 1) else self

    def up(self):
        return Cursor(self.items, self.index - 1) if self.index > 0 else self

    def __eq__(self, other):
        return self.items == other.items and self.index == other.index

    @property
    def current(self):
        return self.items[self.index]
