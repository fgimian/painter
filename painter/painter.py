import sys

from .ansi_styles import styles as ansi_styles
from .ansi_patterns import patterns as ansi_patterns
from .supports_color import supports_color


class Painter(object):

    def __init__(self, styles, patterns, applied_styles=[], enabled=True):
        self.styles = styles
        self.patterns = patterns
        self.applied_styles = applied_styles
        self.enabled = enabled

    def __getattr__(self, name):
        if name not in self.styles and name not in self.patterns:
            raise AttributeError(
                "%r object has no attribute %r" %
                (self.__class__.__name__, name)
            )

        return Painter(
            self.styles, self.patterns, self.applied_styles + [name],
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
                pattern = getattr(self.patterns, applied_style)
                styled_text = pattern(styled_text)
        return styled_text

    def __dir__(self):
        return (
            dir(type(self)) + list(self.__dict__) + list(self.styles) +
            list(self.patterns)
        )

    def __repr__(self):
        return (
            '<%s applied_styles=%r>' %
            (self.__class__.__name__, self.applied_styles)
        )

# Enable ANSI coloring on Windows using Colorama
if sys.platform == 'win32':  # pragma: nocover
    import colorama
    colorama.init()

paint = Painter(ansi_styles, ansi_patterns, enabled=supports_color())
