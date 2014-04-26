from nose.tools import raises

from painter.ansi_styles import ansi
from painter.ansi_styles import AnsiStyle, AnsiStyler  # noqa


def test_return_ansi_escape_codes():
    assert ansi.green.open == '\x1b[32m'
    assert ansi.on_green.open == '\x1b[42m'
    assert ansi.green.close == '\x1b[39m'


def test_ansi_style_repr():
    assert eval(repr(ansi.green)) == ansi.green


@raises(AttributeError)
def test_ansi_raises_exception_on_invalid_color():
    ansi.invalid_color


def test_ansi_styler_repr():
    assert eval(repr(ansi)) == ansi
