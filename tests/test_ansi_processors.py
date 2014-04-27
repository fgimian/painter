from types import FunctionType as function

from nose.tools import raises

from painter.ansi_styles import styles
from painter.ansi_processors import rainbow, zebra, processors
from painter.ansi_processors import AnsiProcessor  # noqa


def test_rainbow():
    assert rainbow('I like rainbows', styles) == (
        styles.red('I') + ' ' + styles.green('l') + styles.blue('i') +
        styles.magenta('k') + styles.red('e') + ' ' + styles.green('r') +
        styles.blue('a') + styles.magenta('i') + styles.red('n') +
        styles.yellow('b') + styles.green('o') + styles.blue('w') +
        styles.magenta('s')
    )


def test_zebra():
    assert zebra('Zebras are cool', styles) == (
        'Z' + styles.inverse('e') + 'b' + styles.inverse('r') + 'a' +
        styles.inverse('s') + ' ' + styles.inverse('a') + 'r' +
        styles.inverse('e') + ' ' + styles.inverse('c') + 'o' +
        styles.inverse('o') + 'l'
    )


def test_ansi_processor_dir():
    for item in [
        '__class__', '__getattr__',  'processors', 'rainbow', 'zebra'
    ]:
        yield check_item_in_ansi_dir, item


def check_item_in_ansi_dir(item):
    return item in dir(processors)


def test_ansi_styler_returns_valid_processor():
    assert isinstance(processors.rainbow, function)


@raises(AttributeError)
def test_ansi_processor_raises_exception_on_invalid_processor():
    processors.invalid_processor


def test_ansi_processor_repr():
    assert eval(repr(processors)) == processors
