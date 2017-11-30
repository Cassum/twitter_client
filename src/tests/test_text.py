from twit_cli.text import Text, Green


def test_text_renders_to_string():
    assert 'test' == str(Text('test'))


def test_text_renders_to_string_with_colors():
    assert 'test it' == str(Text('test', Green(), ' it'))


def test_you_can_add_one_text_to_another():
    assert Text('first') + Text('second') == Text('first', 'second')


def test_you_can_add_one_text_to_another_with_colors():
    assert Text('first') + Text(Green(), 'second') == \
        Text('first', Green(), 'second')
