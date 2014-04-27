# Painter #
*Your own expressive painter who colors text in your terminal*

[![Build Status](https://travis-ci.org/fgimian/painter.png?branch=master)](https://travis-ci.org/fgimian/painter)
[![Coverage Status](https://coveralls.io/repos/fgimian/painter/badge.png)](https://coveralls.io/r/fgimian/painter)
[![License](https://pypip.in/license/painter/badge.png)](https://pypi.python.org/pypi/painter/)
[![Latest Version](https://pypip.in/version/painter/badge.png)](https://pypi.python.org/pypi/painter/)
[![Downloads](https://pypip.in/download/painter/badge.png)](https://pypi.python.org/pypi/painter/)

![Painter Logo](https://raw.githubusercontent.com/fgimian/painter/master/images/painter_logo.png)

Awesome artwork provided courtesy of
[Open Clip Art Library](http://openclipart.org/detail/174634/painter-penguin-by-moini-174634)

Painter is an ANSI coloring library heavily based on the awesome
[chalk](https://github.com/sindresorhus/chalk) library for Node.js along with
all its dependences.  However, painter attempts to provide an even more
expressive API which reads like English.

Painter is fully tested with 100% coverage and also completely Flake8
compilant too!

## Quick Start ##

Install Painter in your virtualenv as follows:

``` bash
pip install painter
```

And now, go ahead and use it to output colors to your terminal:

``` python
from __future__ import print_function

from painter import paint

# Simple printing of colors
print('Welcome to Painter!', paint.red('I can paint things red'),
      paint.blue('and blue'))

# Chaining colors and styles
print(paint.blue.on_red.bold.underline('and far more complex combos too'))
print()

# Nested painting
print(paint.on_red('I can also use a background color across',
                   paint.blue('multiple'), paint.yellow('foreground colors')))

# Custom separator
print(paint('and', 'allow', 'you to use', paint.red('custom separators'),
      sep='-'))
print()

# Creating themes
cool_theme = paint.green.on_red.underline.bold
print('Creating', cool_theme('your own theme'), 'is easy')

# Easily disable painting of colors
paint.enabled = False
print('and I allow you to easily', paint.red('disable'), paint.blue('me'))
print()

paint.enabled = True
print('Hope you have a', paint.blue('lovely day!'), paint.green(':)'))
```

The output of this script looks something like this:

![Painter Demo](https://raw.githubusercontent.com/fgimian/painter/master/images/painter_demo.png)

Complete documentation is coming soon.

## Running Tests ##

You may run the unit tests as follows:

``` bash
git clone https://github.com/fgimian/painter.git
cd painter
python setup.py test
```

## License ##

Painter is released under the MIT License. Please see the
[LICENSE](https://github.com/fgimian/painter/blob/master/LICENSE) file for
more details.

## Changelog ##

*You can click a version name to see a diff with the previous one.*

* **[0.3-dev](https://github.com/fgimian/painter/compare/v0.2...master) (TBA)**
    * Implemented coloring support for Windows using the colorama library.
    * Updated the test command to be run from setup.py to avoid unnecessary
      download af test dependencies during installation.
* **0.2 (2014-04-26)**
    * Initial release
