codes = {
    'reset': (0, 0),

    'bold': (1, 22),
    'italic': (3, 23),
    'underline': (4, 24),
    'blink': (5, 25),
    'inverse': (7, 27),
    'strikethrough': (9, 29),

    'black': (30, 39),
    'red': (31, 39),
    'green': (32, 39),
    'yellow': (33, 39),
    'blue': (34, 39),
    'magenta': (35, 39),
    'cyan': (36, 39),
    'white': (37, 39),
    'gray': (90, 39),

    'on_black': (40, 49),
    'on_red': (41, 49),
    'on_green': (42, 49),
    'on_yellow': (43, 49),
    'on_blue': (44, 49),
    'on_magenta': (45, 49),
    'on_cyan': (46, 49),
    'on_white': (47, 49)
}
codes['grey'] = codes['gray']


class Style(object):
    def __init__(self, open_code, close_code):
        self.open_code = open_code
        self.close_code = close_code

    @property
    def open(self):
        return'\x1b[%im' % self.open_code

    @property
    def close(self):
        return '\x1b[%im' % self.close_code

    def __repr__(self):
        return '%s<Style>%s' % (self.open, self.close)


class Styler(object):
    def __init__(self):
        self.styles = {}
        for key, (open_code, close_code) in codes.items():
            self.styles[key] = Style(open_code, close_code)

    def __contains__(self, key):
        return key in self.styles

    def __getattr__(self, name):
        if name not in self.styles:
            raise AttributeError(
                "'Styler' object has no attribute '%s'" % name
            )

        return self.styles[name]

styles = Styler()
