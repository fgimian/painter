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

## Usage ##

### The Painter ###

``` python
from painter import paint
```

#### Generating Colored Text ####

You may now use the paint instance for all your painting needs.  Simply chain
a foreground color, a background color and any number of style modifiers.

The following are available:

* ***Foreground colors***
    * black
    * red
    * green
    * yellow
    * blue
    * magenta
    * cyan
    * white
    * gray (or grey)
* ***Background colors***
    * on_black
    * on_red
    * on_green
    * on_yellow
    * on_blue
    * on_magenta
    * on_cyan
    * on_white
* ***Style Modifiers***
    * reset
    * bold
    * italic (not widely supported)
    * underline
    * blink
    * inverse
    * strikethrough (not widely supported)

After chaining the various properties of your style, you may call the returned
object with text to obtain an ANSI wrapped version which is ready for printing.

An example of red text on a white background in bold would be:

``` python
print(paint.red.on_black.bold('Hello world!'))
```

Multiple arguments can be passed to the returned object which allow for nesting
of styles.

For example, let's print various text colors on a red background:

``` python
print(paint.on_red('Unstyled', paint.blue('blue'), paint.green('green'),
                   paint.bold('regular color and bold')))
```

Naturally, you can nest any styles you want.  For example, you can start with
bold text and vary the color of various words.

``` python
print(paint.bold('Regular bold', paint.blue('blue'),
                 paint.on_red('red background')))
```

Multiple arguments passed to the paint callable will be separated by a single
white space.  However, you can customise this similarly to the way you do
with the print function.

``` python
print('Hello', paint.cyan('there'), paint.green('buddy'), sep='_')
```

#### Creating Custom Themes ####

You can easily create themes by saving a suitable instance of paint into a
variable and later calling it to invoke the saved style.

For example, let's create a style which provides bold red text on a magenta
background:

``` python
theme = paint.red.on_magenta.bold
```

Simply calling this variable with text from now on will render that style.

``` python
print(theme('My special little theme'))
```

Just like regular styles, themes can also be nested:

``` python
theme_bg = paint.on_white
theme_text_a = paint.red.bold
theme_text_b = paint.blue.underline
print(theme_bg(theme_text_a('Hello'), theme_text_b('world!')))
```

#### Color Support & Enabling or Disabling Colors ####

By default, Painter will attempt to detect if your OS supports colors.  You
may verify the detected color ability by reading the member variable
**supports_color**.

``` python
if paint.supports_color:
    print('Painter detected that your OS supports colors')
else:
    print('Painter detected that your OS does not support colors')
```

Painter will automatically detect enable or disable colors respectively if
the following CLI argument is present; **--color** or **--no-color**.

However, if you would like to explicitly enable or disable coloring, simply
update the boolean member variable **enabled**.

e.g.

``` python
paint.enabled = False
```

### Color Utilities ###

#### Lower-level Access to Styles ####

You may access the open and close string required to print any color or style
using the **styles** member variable.

e.g.

``` python
print(paint.styles.red.open + 'Some red text' + paint.styles.red.close)
```

#### Stripping Color from Strings ####

You may also easily strip color from a string using the **strip_color**
function:

``` python
colored_text = paint.red.on_blue('Text with some color')
uncolored_text = paint.strip_color(colored_text)
```

## Running Tests ##

You may run the unit tests as follows:

``` bash
git clone https://github.com/fgimian/painter.git
cd painter
python setup.py test
```

## License ##

Painter is released under the **MIT** license. Please see the
[LICENSE](https://github.com/fgimian/painter/blob/master/LICENSE) file for
more details.

## Changelog ##

*You can click a version name to see a diff with the previous one.*

* ***[0.3-dev](https://github.com/fgimian/painter/compare/v0.2...master) (TBA)***
    * Implemented coloring support for Windows using the colorama library.
    * Updated the test command to be run from setup.py to avoid unnecessary
      download af test dependencies during installation.
    * Several minor bug fixes.
* ***0.2 (2014-04-26)***
    * Initial release
