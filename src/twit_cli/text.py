from itertools import chain

class Color:
    name = 'default'

    def __init__(self, modificators=None):
        self.modificators = modificators or []

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.modificators == other.modificators
        )

Default = Color


class Black(Color):
    name = 'black'


class Red(Color):
    name = 'red'


class Green(Color):
    name = 'green'


class Yellow(Color):
    name = 'yellow'


class Blue(Color):
    name = 'blue'


class Magenta(Color):
    name = 'magenta'


class Cyan(Color):
    name = 'cyan'


class White(Color):
    name = 'white'


class TextItem:
    def __init__(self, text, color=Color):
        self.text = text
        self.color = color

    def __eq__(self, other):
        return self.text == other.text and self.color == other.color

    def __repr__(self):
        return '<{}, {}: {}>'.format(
            self.color.name,
            self.color.modificators,
            repr(self.text),
        )


class Text:
    def __init__(self, *args):
        color = Default()
        _text = []
        for item in args:
            if isinstance(item, str):
                _text.append(TextItem(item, color))
            else:
                color = item
        self._text = _text

    def __str__(self):
        result = ''
        for item in self._text:
            result += item.text
        return result

    def __repr__(self):
        return repr(self._text)

    def __eq__(self, other):
        return self._text == other._text

    def __add__(self, other):
        if not isinstance(other, Text):
            raise TypeError()
        color = Default()
        result = []
        for item in chain(self._text, other._text):
            if item.color != color:
                color = item.color
                result.append(color)
            result.append(item.text)
        return Text(*result)

    def __iter__(self):
        return iter(self._text)
