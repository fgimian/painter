# Painter #
*Your own expressive painter who colors text in your terminal*

[![Build Status](https://travis-ci.org/fgimian/painter.png?branch=master)](https://travis-ci.org/fgimian/painter)

![Painter Logo](https://raw.githubusercontent.com/fgimian/painter/master/images/painter_logo.png)

Awesome artwork provided courtesy of [Open Clip Art Library](http://openclipart.org/detail/174634/painter-penguin-by-moini-174634)

Painter is heavily based on the awesome [chalk](https://github.com/sindresorhus/chalk) library for Node.js along with all its dependences.  However, painter attempts to provide an even more expressive API which reads like English.

Painter is fully tested with 100% coverage and also completely Flake8 compilant too!

## Quick Start ##

Install Painter in your virtualenv as follows:

``` bash
pip install git+git://github.com/fgimian/painter.git
```

And now, go ahead and use it to output colors to your terminal:

``` python
from __future__ import print_function

from painter import paint

# Simple printing of colors
print('Welcome to Painter!', paint.red('I can paint things red'),
      paint.blue('and blue'))

# Chaining colors
print(paint.blue.on_red.bold.underline('and far more complex combos too'))

# Nested painting
print(paint.on_red('You can also use a background across',
                   paint.blue('multiple'), paint.yellow('foregrounds')))

# Custom separator
print(paint('you', 'can', 'even', 'customise', 'the', 'seperator', sep='-'))

# Easily disable painting of colors
paint.enabled = False
print('You can easily', paint.red('disable'), paint.blue('your painter'))
```

The output of this script looks something like this:

![Painter Demo](https://raw.githubusercontent.com/fgimian/painter/master/images/painter_demo.png)

Complete documentation is coming soon.
