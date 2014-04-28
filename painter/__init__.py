__version__ = '0.3.1'
__author__ = 'Fotis Gimian'
__email__ = 'fgimiansoftware@gmail.com'
__url__ = 'https://github.com/fgimian/painter'
__license__ = 'MIT'
__title__ = 'Painter'

from .ansi_styles import styles  # noqa
from .ansi_patterns import patterns  # noqa
from .painter import paint  # noqa
from .strip_color import strip_color  # noqa
from .supports_color import supports_color  # noqa

__all__ = [
    'styles',
    'patterns',
    'paint',
    'strip_color',
    'supports_color'
]
