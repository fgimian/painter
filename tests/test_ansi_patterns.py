from nose.tools import raises

from painter.ansi_patterns import AnsiPattern, patterns


def test_ansi_pattern_rainbow():
    assert patterns.rainbow('I like rainbows') == (
        '\x1b[31mI\x1b[39m' + ' ' + '\x1b[32ml\x1b[39m' + '\x1b[34mi\x1b[39m' +
        '\x1b[35mk\x1b[39m' + '\x1b[31me\x1b[39m' + ' ' + '\x1b[32mr\x1b[39m' +
        '\x1b[34ma\x1b[39m' + '\x1b[35mi\x1b[39m' + '\x1b[31mn\x1b[39m' +
        '\x1b[33mb\x1b[39m' + '\x1b[32mo\x1b[39m' + '\x1b[34mw\x1b[39m' +
        '\x1b[35ms\x1b[39m'
    )


def test_ansi_pattern_zebra():
    assert patterns.zebra('Zebras are cool') == (
        'Z' + '\x1b[7me\x1b[27m' + 'b' + '\x1b[7mr\x1b[27ma' +
        '\x1b[7ms\x1b[27m' + ' ' + '\x1b[7ma\x1b[27mr' + '\x1b[7me\x1b[27m' +
        ' ' + '\x1b[7mc\x1b[27m' + 'o' + '\x1b[7mo\x1b[27m' + 'l'
    )


def test_ansi_pattern_repr():
    assert repr(patterns.rainbow) == "<AnsiPattern function='rainbow'>"


def test_ansi_pattern_dir():
    for item in [
        '__class__', '__getattr__',  'patterns', 'rainbow', 'zebra'
    ]:
        yield check_item_in_ansi_dir, item


def check_item_in_ansi_dir(item):
    return item in dir(patterns)


def test_ansi_patterner_registration_of_custom_pattern():
    def underline_vowels(text, styles):
        vowel_text = ''
        for char in text:
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowel_text += styles.underline(char)
            else:
                vowel_text += char
        return vowel_text
    patterns.register('voweler', underline_vowels)
    assert 'voweler' in patterns
    voweler_text = patterns.voweler('Hi there')
    patterns.deregister('voweler')
    assert 'voweler' not in patterns
    assert voweler_text == (
        'H' + '\x1b[4mi\x1b[24m' + ' th' + '\x1b[4me\x1b[24m' + 'r' +
        '\x1b[4me\x1b[24m'
    )


@raises(KeyError)
def test_ansi_patterner_invalid_deregistration():
    patterns.deregister('foo')


def test_ansi_patterner_returns_valid_pattern():
    assert isinstance(patterns.rainbow, AnsiPattern)


@raises(AttributeError)
def test_ansi_patterner_raises_exception_on_invalid_patterner():
    patterns.invalid_pattern


def test_ansi_patterner_repr():
    assert repr(patterns) == (
        '<AnsiPatterner patterns=%r>' % sorted(list(patterns))
    )
