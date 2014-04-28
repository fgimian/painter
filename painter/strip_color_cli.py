#!/usr/bin/env python
from __future__ import print_function
import sys
import codecs

from . import __version__
from .strip_color import strip_color


def main():
    try:
        input = sys.argv[1]
    except IndexError:
        input = None

    if '-h' in sys.argv or '--help' in sys.argv:
        print('strip-color <input file> > <output file>')
        print('or')
        print('cat <input file> | strip-color > <output file>')
    elif '-v' in sys.argv or '--version' in sys.argv:
        print(__version__)
    else:
        try:
            if input:
                try:
                    with codecs.open(input, 'r', 'utf-8') as f:
                        sys.stdout.write(strip_color(f.read()))
                except (OSError, IOError) as e:
                    print('%s' % e, file=sys.stderr)
                    exit(e.errno)
            else:
                sys.stdout.write(strip_color(sys.stdin.read()))
        except KeyboardInterrupt:  # pragma: nocover
            exit(1)

if __name__ == '__main__':
    main()
