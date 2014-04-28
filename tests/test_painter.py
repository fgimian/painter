from nose.tools import raises

from painter.painter import paint

paint.enabled = True


def test_painter_style_string():
    assert paint.underline('foo') == '\x1b[4mfoo\x1b[24m'
    assert paint.red('foo') == '\x1b[31mfoo\x1b[39m'
    assert paint.on_red('foo') == '\x1b[41mfoo\x1b[49m'


def test_painter_pattern_string():
    assert paint.rainbow('fooooo o') == (
        '\x1b[31mf\x1b[39m' + '\x1b[33mo\x1b[39m' + '\x1b[32mo\x1b[39m' +
        '\x1b[34mo\x1b[39m' + '\x1b[35mo\x1b[39m' + '\x1b[31mo\x1b[39m' + ' ' +
        '\x1b[32mo\x1b[39m'
    )
    assert paint.zebra('foo') == 'f' + '\x1b[7mo\x1b[27m' + 'o'


def test_painter_support_applying_multiple_styles_at_once():
    assert paint.red.on_green.underline('foo') == (
        '\x1b[4m\x1b[42m\x1b[31mfoo\x1b[39m\x1b[49m\x1b[24m'
    )
    assert paint.underline.red.on_green('foo') == (
        '\x1b[42m\x1b[31m\x1b[4mfoo\x1b[24m\x1b[39m\x1b[49m'
    )


def test_painter_support_applying_pattern_and_style_at_once():
    assert paint.zebra.red('foo') == (
        '\x1b[31mf\x1b[7m' + 'o' + '\x1b[27mo\x1b[39m'
    )


def test_painter_support_nesting_styles():
    assert paint.red('foo' + paint.underline.on_blue('bar') + '!') == (
        '\x1b[31mfoo\x1b[44m\x1b[4mbar\x1b[24m\x1b[49m!\x1b[39m'
    )


def test_painter_reset_all_styles_with_reset():
    assert paint.reset(paint.red.on_green.underline('foo') + 'foo') == (
        '\x1b[0m\x1b[4m\x1b[42m\x1b[31mfoo\x1b[39m\x1b[49m\x1b[24mfoo\x1b[0m'
    )


def test_painter_supports_grey():
    assert paint.grey('foo') == '\x1b[90mfoo\x1b[39m'


def test_painter_support_variable_number_of_arguments():
    assert paint.red('foo', 'bar') == '\x1b[31mfoo bar\x1b[39m'


def test_painter_support_falsy_values():
    assert paint.red(0) == '\x1b[31m0\x1b[39m'


@raises(AttributeError)
def test_painter_raises_exception_on_invalid_color():
    paint.red.invalid_color('this should not be printed')


def test_painter_repr():
    assert repr(paint.red.on_blue.bold.underline) == (
        "<Painter applied_styles=['red', 'on_blue', 'bold', 'underline']>"
    )


def test_painter_dir():
    for item in [
        '__class__', '__getattr__', 'applied_styles', 'enabled',
        'black', 'inverse', 'italic', 'on_blue', 'on_cyan'
    ]:
        yield check_item_in_paint, item


def check_item_in_paint(item):
    return item in dir(paint)


def test_painter_doesnt_output_escape_codes_if_the_input_is_empty():
    assert paint.red() == ''


def test_painter_enabled_does_not_output_colors_when_manually_disabled():
    paint.enabled = False
    assert paint.red('foo') == 'foo'
    paint.enabled = True


def test_painter_styles_exposes_the_styles_as_ansi_escape_codes():
    assert paint.styles.red.open == '\x1b[31m'
