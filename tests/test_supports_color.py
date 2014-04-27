import os
import sys

import mock

from painter.supports_color import supports_color


class TestHasColor:

    def setup(self):
        sys.argv = []
        sys.platform = ''
        os.environ = {}

    @mock.patch('sys.stdout.isatty', return_value=False)
    def test_supports_color_false_if_not_tty(self, mock_isatty):
        assert not supports_color()

    @mock.patch('sys.stdout.isatty', return_value=True)
    def test_supports_color_false_if_no_color_flag_is_used(self, mock_isatty):
        sys.argv = ['--no-color']
        assert not supports_color()

    @mock.patch('sys.stdout.isatty', return_value=True)
    def test_supports_color_true_if_platform_is_win32(self, mock_isatty):
        sys.platform = 'win32'
        assert supports_color()

    @mock.patch('sys.stdout.isatty', return_value=True)
    def test_supports_color_true_if_color_flag_is_used(self, mock_isatty):
        sys.argv = ['--color']
        assert supports_color()

    @mock.patch('sys.stdout.isatty', return_value=True)
    def test_supports_color_false_if_term_is_dumb(self, mock_isatty):
        os.environ['TERM'] = 'dumb'
        assert not supports_color()

    @mock.patch('sys.stdout.isatty', return_value=True)
    def test_supports_color_true_if_colorterm_is_in_env(self, mock_isatty):
        os.environ['COLORTERM'] = 'True'
        assert supports_color()

    def test_supports_color_true_if_valid_term_is_set(self):
        for term in [
            'screen', 'screen' 'xterm', 'xterm256', 'vt100', 'color',
            'ilikecolor', 'ansi', 'cygwin', 'linux', 'linuxrocks'
        ]:
            yield self.check_color_with_env, term

    @mock.patch('sys.stdout.isatty', return_value=True)
    def check_color_with_env(self, mock_isatty, term):
        os.environ['TERM'] = term
        assert supports_color()

    @mock.patch('sys.stdout.isatty', return_value=True)
    def test_supports_color_false_if_no_conditions_are_met(self, mock_isatty):
        assert not supports_color()
