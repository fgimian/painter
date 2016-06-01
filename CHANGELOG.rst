Changelog
---------

`Unreleased <https://github.com/fgimian/painter/tree/master>`_
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- TBA

`Full Source Code Changelog <https://github.com/fgimian/painter/compare/v0.3.1...master>`_

`0.3.1 <https://github.com/fgimian/painter/releases/tag/v0.3.1>`_ (2014-04-29)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Made strip-color CLI script more robust when errors occur

`Full Source Code Changelog <https://github.com/fgimian/painter/compare/v0.3...v0.3.1>`_

`0.3 <https://github.com/fgimian/painter/releases/tag/v0.3>`_ (2014-04-28)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

- Implemented coloring support for Windows using the colorama
  library.
- Updated the test command to be run from setup.py to avoid
  unnecessary download of test dependencies during installation.
- Renamed several of the utility functions for better consistency.
  The paint API is unaffected by these changes.
- The has_color variable is renamed to supports_color and should
  now be used as a function.
- Implemented color patterns which generate varying color patterns
  on strings. The rainbow and zebra patterns come included.
- Custom pattern functions may now be written and easily registered
  with Painter.
- Several bug fixes.

`Full Source Code Changelog <https://github.com/fgimian/painter/compare/v0.2...v0.3>`_

`0.2 <https://github.com/fgimian/painter/releases/tag/v0.2>`_ (2014-04-26)
++++++++++++++++

- Initial release
