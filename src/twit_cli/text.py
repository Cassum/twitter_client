class Color:
    name = 'default'

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


class Text:
    def __init__(self, *args):
        color = Color
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
