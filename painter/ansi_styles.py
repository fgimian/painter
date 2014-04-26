ANSI_CODES = {
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
    'grey': (90, 39),

    'on_black': (40, 49),
    'on_red': (41, 49),
    'on_green': (42, 49),
    'on_yellow': (43, 49),
    'on_blue': (44, 49),
    'on_magenta': (45, 49),
    'on_cyan': (46, 49),
    'on_white': (47, 49)
}


class AnsiStyle(object):
    def __init__(self, open_code, close_code):
        self.open_code = open_code
        self.close_code = close_code

    @property
    def open(self):
        return '\x1b[%im' % self.open_code

    @property
    def close(self):
        return '\x1b[%im' % self.close_code

    def __eq__(self, other):
        return (
            self.open_code == other.open_code and
            self.close_code == other.close_code
        )

    def __repr__(self):
        return (
            'AnsiStyle(open_code=%i, close_code=%i)' %
            (self.open_code, self.close_code)
        )


class AnsiStyler(object):
    def __init__(self):
        self.styles = {}
        for key, (open_code, close_code) in ANSI_CODES.items():
            self.styles[key] = AnsiStyle(open_code, close_code)

    def __contains__(self, key):
        return key in self.styles

    def __getattr__(self, name):
        if name not in self.styles:
            raise AttributeError(
                "'AnsiStyler' object has no attribute '%s'" % name
            )
        return self.styles[name]

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__) + list(self.styles)

    def __eq__(self, other):
        return self.styles == other.styles

    def __iter__(self):
        for style in self.styles:
            yield style

    def __repr__(self):
        return 'AnsiStyler()'

ansi = AnsiStyler()
