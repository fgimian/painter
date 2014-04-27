import subprocess

from painter.strip_color import strip_color


def test_strip_color_from_string():
    assert strip_color(
        '\x1b[0m\x1b[4m\x1b[42m\x1b[31mfoo\x1b[39m\x1b[49m\x1b[24mfoo\x1b[0m'
    ) == 'foofoo'


def test_strip_color_other_sequence_from_string():
    assert strip_color('\x1b[0;33;49;3;9;4mbar\x1b[0m') == 'bar'


def test_strip_color_non_string():
    assert strip_color(['hello', 'there']) == ['hello', 'there']


def test_strip_color_cli():
    stdout, stderr = subprocess.Popen(
        'echo "\x1b[0m\x1b[4m\x1b[42m\x1b[31mfoo'
        '\x1b[39m\x1b[49m\x1b[24mfoo\x1b[0m" | '
        'python -m painter.strip_color_cli',
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).communicate()
    assert stdout == b'foofoo\n'
