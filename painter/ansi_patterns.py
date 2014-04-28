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


class AnsiPatterner(object):
    def __init__(self, patterns):
        self.patterns = patterns

    def __getattr__(self, name):
        if name not in self.patterns:
            raise AttributeError(
                "%r object has no attribute %r" %
                (self.__class__.__name__, name)
            )
        return self.patterns[name]

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

patterns = AnsiPatterner(ANSI_FUNCTIONS)
