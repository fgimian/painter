from nose.tools import raises

from painter.ansi_styles import ansi
from painter.ansi_styles import AnsiStyle, AnsiStyler  # noqa


def test_return_ansi_escape_codes():
    assert ansi.green.open == '\x1b[32m'
    assert ansi.on_green.open == '\x1b[42m'
    assert ansi.green.close == '\x1b[39m'


def test_ansi_style_repr():
    assert eval(repr(ansi.green)) == ansi.green


def test_ansi_style_dir():
    for item in [
        '__class__', '__getattr__',  'styles',
        'black', 'inverse', 'italic', 'on_blue', 'on_cyan'
    ]:
        yield check_item_in_ansi_dir, item


def check_item_in_ansi_dir(item):
    return item in dir(ansi)


@raises(AttributeError)
def test_ansi_raises_exception_on_invalid_color():
    ansi.invalid_color


def test_ansi_styler_repr():
    assert eval(repr(ansi)) == ansi
