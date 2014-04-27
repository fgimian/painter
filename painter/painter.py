import sys

from .ansi_styles import styles as ansi_styles
from .ansi_processors import processors as ansi_processors
from .supports_color import supports_color


class Painter(object):

    def __init__(self, styles, processors, applied_styles=[], enabled=True):
        self.styles = styles
        self.processors = processors
        self.applied_styles = applied_styles
        self.enabled = enabled

    def __getattr__(self, name):
        if name not in self.styles and name not in self.processors:
            raise AttributeError(
                "'Painter' object has no attribute '%s'" % name
            )

        return Painter(
            self.styles, self.processors, self.applied_styles + [name],
            enabled=self.enabled
        )

    def __call__(self, *text, **params):
        sep = params.pop('sep', ' ')
        combined_text = sep.join(str(t) for t in text)
        if not self.enabled or not combined_text:
            return combined_text

        styled_text = combined_text
        for applied_style in self.applied_styles:
            if applied_style in self.styles:
                style = getattr(self.styles, applied_style)
                styled_text = style(styled_text)
            else:
                processor = getattr(self.processors, applied_style)
                styled_text = processor(styled_text, self.styles)
        return styled_text

    def __dir__(self):
        return (
            dir(type(self)) + list(self.__dict__) + list(self.styles) +
            list(self.processors)
        )

    def __eq__(self, other):
        return (
            self.styles == other.styles and
            self.processors == other.processors and
            self.applied_styles == other.applied_styles and
            self.enabled == other.enabled
        )

    def __repr__(self):
        return (
            'Painter(styles=%r, processors=%r, applied_styles=%r, '
            'enabled=%r)' %
            (self.styles, self.processors, self.applied_styles, self.enabled)
        )

# Enable ANSI coloring on Windows using Colorama
if sys.platform == 'win32':  # pragma: nocover
    import colorama
    colorama.init()

paint = Painter(ansi_styles, ansi_processors, enabled=supports_color())
