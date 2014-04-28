import re


def strip_color(s):
    if isinstance(s, str):
        return re.sub(r"""
            \x1b            # escape character
            \[              # the CSI code for color
            (               # start of color definition
            [0-9]{1,3}      # the ANSI color code
            (;[0-9]{1,3})*  # optional ANSI color properties (mainly xterm)
            )?              # end of color definition
            m               # the CSI SGR (Select Graphic Rendition) command
        """, '', s, flags=re.VERBOSE)
    else:
        return s
