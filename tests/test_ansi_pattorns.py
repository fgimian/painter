from types import FunctionType as function

from nose.tools import raises

from painter.ansi_styles import styles
from painter.ansi_patterns import rainbow, zebra, patterns


def test_rainbow():
    assert rainbow('I like rainbows', styles) == (
        '\x1b[31mI\x1b[39m' + ' ' + '\x1b[32ml\x1b[39m' + '\x1b[34mi\x1b[39m' +
        '\x1b[35mk\x1b[39m' + '\x1b[31me\x1b[39m' + ' ' + '\x1b[32mr\x1b[39m' +
        '\x1b[34ma\x1b[39m' + '\x1b[35mi\x1b[39m' + '\x1b[31mn\x1b[39m' +
        '\x1b[33mb\x1b[39m' + '\x1b[32mo\x1b[39m' + '\x1b[34mw\x1b[39m' +
        '\x1b[35ms\x1b[39m'
    )


def test_zebra():
    assert zebra('Zebras are cool', styles) == (
        'Z' + '\x1b[7me\x1b[27m' + 'b' + '\x1b[7mr\x1b[27ma' +
        '\x1b[7ms\x1b[27m' + ' ' + '\x1b[7ma\x1b[27mr' + '\x1b[7me\x1b[27m' +
        ' ' + '\x1b[7mc\x1b[27m' + 'o' + '\x1b[7mo\x1b[27m' + 'l'
    )


def test_ansi_pattern_dir():
    for item in [
        '__class__', '__getattr__',  'patterns', 'rainbow', 'zebra'
    ]:
        yield check_item_in_ansi_dir, item


def check_item_in_ansi_dir(item):
    return item in dir(patterns)


def test_ansi_styler_returns_valid_patterner():
    assert isinstance(patterns.rainbow, function)


@raises(AttributeError)
def test_ansi_pattern_raises_exception_on_invalid_patterner():
    patterns.invalid_pattern


def test_ansi_pattern_repr():
    assert repr(patterns) == (
        '<AnsiPatterner patterns=%r>' % sorted(list(patterns))
    )
