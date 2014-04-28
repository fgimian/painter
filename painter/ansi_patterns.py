from .ansi_styles import styles as ansi_styles


def rainbow(text, styles):
    rainbow = [
        styles.red, styles.yellow, styles.green, styles.blue, styles.magenta
    ]
    rainbow_text = ''
    for index, char in enumerate(text):
        if char in [' ', '\t', '\r', '\n']:
            rainbow_text += char
        else:
            rainbow_text += rainbow[index % len(rainbow)](char)
    return rainbow_text


def zebra(text, styles):
    zebra_text = ''
    for index, char in enumerate(text):
        if index % 2 == 0:
            zebra_text += char
        else:
            zebra_text += styles.inverse(char)
    return zebra_text


ANSI_FUNCTIONS = {
    'rainbow': rainbow,
    'zebra': zebra
}


class AnsiPattern(object):
    def __init__(self, function, styles):
        self.function = function
        self.styles = styles

    def __call__(self, text):
        return self.function(text, self.styles)

    def __repr__(self):
        return (
            '<%s function=%r>' %
            (self.__class__.__name__, self.function.__name__)
        )


class AnsiPatterner(object):
    def __init__(self, patterns, styles):
        self.patterns = patterns
        self.styles = styles

    def register(self, name, function):
        self.patterns[name] = function

    def deregister(self, name):
        del self.patterns[name]

    def __getattr__(self, name):
        if name not in self.patterns:
            raise AttributeError(
                "%r object has no attribute %r" %
                (self.__class__.__name__, name)
            )
        return AnsiPattern(self.patterns[name], self.styles)

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__) + list(self.patterns)

    def __iter__(self):
        for pattern in self.patterns:
            yield pattern

    def __repr__(self):
        return (
            '<%s patterns=%r>' %
            (self.__class__.__name__, sorted(list(self.patterns)))
        )

patterns = AnsiPatterner(ANSI_FUNCTIONS, ansi_styles)
