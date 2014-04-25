import re


def strip_ansi(s):
    if isinstance(s, str):
        return re.sub(
            r'\x1B\[([0-9]{1,2}(;[0-9]{1,2})*)?[m|K]', '', s
        )
    else:
        return s
