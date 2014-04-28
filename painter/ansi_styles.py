ANSI_CODES = {
    'reset': (0, 0),

    'bold': (1, 22),
    'faint': (2, 22),
    'italic': (3, 23),
    'underline': (4, 24),
    'blinking': (5, 25),
    'inverse': (7, 27),
    'invisible': (8, 28),
    'strikethrough': (9, 29),

    'black': (30, 39),
    'red': (31, 39),
    'green': (32, 39),
    'yellow': (33, 39),
    'blue': (34, 39),
    'magenta': (35, 39),
    'cyan': (36, 39),
    'white': (37, 39),

    'light_black': (90, 39),
    'light_red': (91, 39),
    'light_green': (92, 39),
    'light_yellow': (93, 39),
    'light_blue': (94, 39),
    'light_magenta': (95, 39),
    'light_cyan': (96, 39),
    'light_white': (97, 39),

    'on_black': (40, 49),
    'on_red': (41, 49),
    'on_green': (42, 49),
    'on_yellow': (43, 49),
    'on_blue': (44, 49),
    'on_magenta': (45, 49),
    'on_cyan': (46, 49),
    'on_white': (47, 49),

    'on_light_black': (100, 49),
    'on_light_red': (101, 49),
    'on_light_green': (102, 49),
    'on_light_yellow': (103, 49),
    'on_light_blue': (104, 49),
    'on_light_magenta': (105, 49),
    'on_light_cyan': (106, 49),
    'on_light_white': (107, 49)
}

# Setting up a few handy aliases & alternative spellings for ease of use
ANSI_CODES['gray'] = ANSI_CODES['light_black']
ANSI_CODES['grey'] = ANSI_CODES['light_black']
ANSI_CODES['on_gray'] = ANSI_CODES['on_light_black']
ANSI_CODES['on_grey'] = ANSI_CODES['on_light_black']


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

    def __call__(self, text):
        return self.open + text + self.close

    def __repr__(self):
        return (
            '<%s open_code=%r, close_code=%r>' %
            (self.__class__.__name__, self.open_code, self.close_code)
        )


class AnsiStyler(object):
    def __init__(self, styles):
        self.styles = styles

    def __getattr__(self, name):
        if name not in self.styles:
            raise AttributeError(
                "%r object has no attribute %r" %
                (self.__class__.__name__, name)
            )
        open_code, close_code = self.styles[name]
        return AnsiStyle(open_code, close_code)

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__) + list(self.styles)

    def __iter__(self):
        for style in self.styles:
            yield style

    def __repr__(self):
        return (
            '<%s styles=%r>' %
            (self.__class__.__name__, sorted(list(self.styles)))
        )

styles = AnsiStyler(ANSI_CODES)
