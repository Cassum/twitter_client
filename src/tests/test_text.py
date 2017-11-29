from twit_cli.text import Text, Green


def test_text_renders_to_string():
    assert 'test' == str(Text('test'))


def test_text_renders_to_string_with_colors():
    assert 'test it' == str(Text('test', Green, ' it'))
