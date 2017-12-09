from twit_cli.cursor import Cursor


def test_it_can_move_down():
    cur = Cursor(['foo', 'bar'], 0)
    assert Cursor(['foo', 'bar'], 1) == cur.down()


def test_it_can_move_up():
    cur = Cursor(['foo', 'bar'], 1)
    assert Cursor(['foo', 'bar'], 0) == cur.up()


def test_it_cant_go_over_limits():
    cur = Cursor(['foo', 'bar'], 0)
    assert Cursor(['foo', 'bar'], 0) == cur.up()
    cur = Cursor(['foo', 'bar'], 1)
    assert Cursor(['foo', 'bar'], 1) == cur.down()


def test_it_shows_current_item():
    cur = Cursor(['foo', 'bar'], 1)
    assert cur.current == 'bar'
