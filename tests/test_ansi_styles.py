from nose.tools import raises

from painter.ansi_styles import ansi


def test_return_ansi_escape_codes():
    assert ansi.green.open == '\x1b[32m'
    assert ansi.on_green.open == '\x1b[42m'
    assert ansi.green.close == '\x1b[39m'


def test_return_ansi_repr():
    assert repr(ansi.green) == '\x1b[32m<Style>\x1b[39m'


@raises(AttributeError)
def test_ansi_raises_exception_on_invalid_color():
    ansi.invalid_color
