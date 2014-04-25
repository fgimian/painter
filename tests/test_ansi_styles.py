from painter.ansi_styles import styles as ansi


def test_return_ansi_escape_codes():
    assert ansi['green'].open == '\x1b[32m'
    assert ansi['on_green'].open == '\x1b[42m'
    assert ansi['green'].close == '\x1b[39m'


def test_return_ansi_repr():
    assert ansi['green'].__repr__() == '\x1b[32m<Style>\x1b[39m'
