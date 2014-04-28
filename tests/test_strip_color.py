import os
import sys
import subprocess

import painter
from painter.painter import paint
from painter.strip_color import strip_color


if sys.version_info[0] == 2:
    def b(s):
        return s
else:
    def b(s):
        return s.encode("latin-1")


def test_strip_color_from_string():
    assert strip_color(
        '\x1b[0m\x1b[4m\x1b[42m\x1b[31mfoo\x1b[39m\x1b[49m\x1b[24mfoo\x1b[0m'
    ) == 'foofoo'


def test_strip_color_from_ls_output():
    fixtures_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'fixtures')
    )
    with open(os.path.join(fixtures_dir, 'ls_output_colored.txt')) as f:
        colored_text = f.read()
    with open(os.path.join(fixtures_dir, 'ls_output.txt')) as f:
        text = f.read()
    assert strip_color(colored_text) == text


def test_strip_color_other_sequence_from_string():
    assert strip_color('\x1b[0;33;49;3;9;4mbar\x1b[0m') == 'bar'


def test_strip_color_non_string():
    assert strip_color(['hello', 'there']) == ['hello', 'there']


def test_strip_color_strips_color_from_painter():
    assert strip_color(paint.underline.red.on_green('foo')) == 'foo'


def test_strip_color_cli_version():
    stdout, stderr = subprocess.Popen(
        'python -m painter.strip_color_cli -v',
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).communicate()
    assert stdout == b(painter.__version__ + '\n')


def test_strip_color_cli_help():
    stdout, stderr = subprocess.Popen(
        'python -m painter.strip_color_cli -h',
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).communicate()
    assert b'<input file> > <output file>' in stdout


def test_strip_color_cli_stdin():
    stdout, stderr = subprocess.Popen(
        'echo "\x1b[0m\x1b[4m\x1b[42m\x1b[31mfoo'
        '\x1b[39m\x1b[49m\x1b[24mfoo\x1b[0m" | '
        'python -m painter.strip_color_cli',
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).communicate()
    assert stdout == b'foofoo\n'


def test_strip_color_cli_file():
    fixtures_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'fixtures')
    )

    input_file = os.path.join(fixtures_dir, 'ls_output_colored.txt')
    stdout, stderr = subprocess.Popen(
        'python -m painter.strip_color_cli %s' % input_file,
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ).communicate()

    with open(os.path.join(fixtures_dir, 'ls_output.txt')) as f:
        text = f.read()

    assert stdout == b(text)
