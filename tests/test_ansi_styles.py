from nose.tools import raises

from painter.ansi_styles import styles
from painter.ansi_styles import AnsiStyle


def test_ansi_style_return_escape_codes():
    assert styles.green.open == '\x1b[32m'
    assert styles.on_green.open == '\x1b[42m'
    assert styles.green.close == '\x1b[39m'


def test_ansi_style_repr():
    assert repr(styles.green) == '<AnsiStyle open_code=32, close_code=39>'


def test_ansi_styler_dir():
    for item in [
        '__class__', '__getattr__',  'styles',
        'black', 'inverse', 'italic', 'on_blue', 'on_cyan'
    ]:
        yield check_item_in_ansi_dir, item


def check_item_in_ansi_dir(item):
    return item in dir(styles)


def test_ansi_styler_returns_valid_color():
    assert isinstance(styles.green, AnsiStyle)


@raises(AttributeError)
def test_ansi_styler_raises_exception_on_invalid_color():
    styles.invalid_color


def test_ansi_styler_repr():
    assert repr(styles) == '<AnsiStyler styles=%r>' % sorted(list(styles))
