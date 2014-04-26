#!/usr/bin/env python
from __future__ import print_function
import sys
import codecs

from . import __version__
from .strip_ansi import strip_ansi


def main():
    try:
        input = sys.argv[1]
    except IndexError:
        input = None

    if '-h' in sys.argv or '--help' in sys.argv:
        print('strip-ansi <input file> > <output file>')
        print('or')
        print('cat <input file> | strip-ansi > <output file>')
        exit()

    if '-v' in sys.argv or '--version' in sys.argv:
        print(__version__)
        exit()

    if input:
        with codecs.open(input, 'r', 'utf-8') as f:
            sys.stdout.write(strip_ansi(f.read()))
            exit()

    sys.stdout.write(strip_ansi(sys.stdin.read()))

if __name__ == '__main__':
    main()
