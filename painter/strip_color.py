import sys
import re


if sys.version_info[0] == 2:  # pragma: nocover
    string_type = basestring  # noqa
else:  # pragma: nocover
    string_type = str


def strip_color(s):
    if isinstance(s, string_type):
        return re.compile(r"""
            \x1b            # escape character
            \[              # the CSI code for color
            (               # start of color definition
            [0-9]{1,3}      # the ANSI color code
            (;[0-9]{1,3})*  # optional ANSI color properties (mainly xterm)
            )?              # end of color definition
            m               # the CSI SGR (Select Graphic Rendition) command
        """, re.VERBOSE).sub('', s)
    else:
        return s
