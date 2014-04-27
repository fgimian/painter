import sys

from .ansi_styles import styles as ansi_styles
from .supports_color import supports_color


class Painter(object):

    def __init__(self, styles, applied_styles=[], enabled=True):
        self.applied_styles = applied_styles
        self.styles = styles
        self.enabled = enabled

    def __getattr__(self, name):
        if name not in self.styles:
            raise AttributeError(
                "'Painter' object has no attribute '%s'" % name
            )

        sub_painter = Painter(
            self.styles, self.applied_styles + [name], enabled=self.enabled
        )
        return sub_painter

    def __call__(self, *text, **params):
        sep = params.pop('sep', ' ')
        combined_text = sep.join(str(t) for t in text)
        if not self.enabled or not combined_text:
            return combined_text

        styled_text = combined_text
        for applied_style in self.applied_styles:
            style = getattr(self.styles, applied_style)
            styled_text = style.apply(styled_text)
        return styled_text

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__) + list(self.styles)

    def __eq__(self, other):
        return (
            self.applied_styles == other.applied_styles and
            self.styles == other.styles and
            self.enabled == other.enabled
        )

    def __repr__(self):
        return (
            'Painter(styles=%r, applied_styles=%r, enabled=%r)' %
            (self.styles, self.applied_styles, self.enabled)
        )

# Enable ANSI coloring on Windows using Colorama
if sys.platform == 'win32':  # pragma: nocover
    import colorama
    colorama.init()

paint = Painter(ansi_styles, enabled=supports_color())
