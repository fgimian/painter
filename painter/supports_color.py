import os
import sys


def supports_color():
    if '--no-color' in sys.argv:
        return False

    if '--color' in sys.argv:
        return True

    if not sys.stdout.isatty():
        return False

    if sys.platform == 'win32':
        return True

    if 'COLORTERM' in os.environ:
        return True

    term = os.environ.get('TERM', '')

    if term == 'dumb':
        return False

    if (
        any([s for s in ['screen', 'xterm', 'vt100'] if term.startswith(s)]) or
        any([s for s in ['color', 'ansi', 'cygwin', 'linux'] if s in term])
    ):
        return True

    return False
