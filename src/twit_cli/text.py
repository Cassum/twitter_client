class Color:
    name = 'default'

class Green(Color):
    name = 'green'


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
