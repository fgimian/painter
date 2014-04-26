from .ansi_styles import ansi
from .strip_ansi import strip_ansi
from .has_color import has_color


class Painter(object):

    def __init__(self, applied_styles=[], enabled=None):
        self.applied_styles = applied_styles
        self.styles = ansi
        self.strip_color = strip_ansi
        self.supports_color = has_color
        if enabled is None:
            self.enabled = self.supports_color
        else:
            self.enabled = enabled

    def __getattr__(self, name):
        if name not in self.styles:
            raise AttributeError(
                "'Painter' object has no attribute '%s'" % name
            )

        sub_painter = Painter(
            self.applied_styles + [name], enabled=self.enabled
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
            styled_text = style.open + styled_text + style.close
        return styled_text

    def __dir__(self):
        return dir(type(self)) + list(self.__dict__) + list(paint.styles)

    def __eq__(self, other):
        return (
            self.applied_styles == other.applied_styles and
            self.styles == other.styles and
            self.strip_color == other.strip_color and
            self.supports_color == other.supports_color and
            self.enabled == other.enabled
        )

    def __repr__(self):
        return (
            'Painter(applied_styles=%r, enabled=%r)' %
            (self.applied_styles, self.enabled)
        )

paint = Painter()
