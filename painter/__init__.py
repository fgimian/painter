__version__ = '0.3-dev'
__author__ = 'Fotis Gimian'
__email__ = 'fgimiansoftware@gmail.com'
__url__ = 'https://github.com/fgimian/painter'
__license__ = 'MIT'
__title__ = 'Painter'

from .ansi_styles import ansi  # noqa
from .supports_color import supports_color  # noqa
from .painter import paint  # noqa
from .strip_color import strip_color  # noqa

__all__ = [
    'ansi',
    'supports_color',
    'paint',
    'strip_color'
]
