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


class AnsiProcessor(object):
    def __init__(self, processors):
        self.processors = processors

    def __getattr__(self, name):
        if name not in self.processors:
            raise AttributeError(
                "'AnsiProcessor' object has no attribute '%s'" % name
            )
        return self.processors[name]

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__) + list(self.processors)

    def __iter__(self):
        for processor in self.processors:
            yield processor

    def __repr__(self):
        return (
            '<%s processors=%r>' %
            (self.__class__.__name__, sorted(list(self.processors)))
        )

processors = AnsiProcessor(ANSI_FUNCTIONS)
