# Painter #
*Your own expressive painter who colors text in your terminal*

[![Build Status](https://travis-ci.org/fgimian/painter.png?branch=master)](https://travis-ci.org/fgimian/painter)
[![Coverage Status](https://coveralls.io/repos/fgimian/painter/badge.png)](https://coveralls.io/r/fgimian/painter)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://pypi.python.org/pypi/painter/)
[![Latest Version](https://img.shields.io/pypi/v/painter.svg)](https://pypi.python.org/pypi/painter/)

[![Painter Logo](https://raw.githubusercontent.com/fgimian/painter/master/images/painter_logo.png)

Awesome artwork provided courtesy of
[Open Clip Art Library](http://openclipart.org/detail/174634/painter-penguin-by-moini-174634)

Painter is an ANSI coloring library based on the excellent
[chalk](https://github.com/sindresorhus/chalk) and
[colors.js](https://github.com/marak/colors.js/)
libraries for Node.js.  However, painter attempts to provide an even more
expressive API which reads like English.

Painter is fully tested with 100% coverage and also completely Flake8
compliant too!

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

# Using color patterns
print(paint.rainbow('Awww look, a pretty rainbow :)'))
print(paint.zebra('and a scary looking zebra!'))
print()

# Nested painting
print(paint.on_red('I can also use a background color across',
                   paint.blue('multiple'),
                   paint.yellow('foreground colors')))

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

The output of the script above looks something like this:

![Painter Demo](https://raw.githubusercontent.com/fgimian/painter/master/images/painter_demo.png)

## Usage ##

### The Painter ###

Start by importing your painter as follows:

``` python
from painter import paint
```

#### Generating Colored Text ####

You may now use the **paint** instance for all your painting needs.  Simply
chain any combination of a foreground color, a background color, style
modifiers and color patterns.

The following are available:

* ***Foreground colors***
    * Standard colors most commonly supported
        * black
        * red
        * green
        * yellow
        * blue
        * magenta
        * cyan
        * white
    * Extended colors for systems supporting up to 16 colors
        * light_black (or gray / grey)
        * light_red
        * light_green
        * light_yellow
        * light_blue
        * light_magenta
        * light_cyan
        * light_white
* ***Background colors***
    * Standard colors most commonly supported
        * on_black
        * on_red
        * on_green
        * on_yellow
        * on_blue
        * on_magenta
        * on_cyan
        * on_white
    * Extended colors for systems supporting up to 16 colors
        * on_light_black (or on_gray / on_grey)
        * on_light_red
        * on_light_green
        * on_light_yellow
        * on_light_blue
        * on_light_magenta
        * on_light_cyan
        * on_light_white
* ***Style Modifiers***
    * Styles most commonly supported
        * reset
        * bold
        * underline
        * blinking
        * inverse
    * Not widely supported
        * faint
        * italic
        * invisible
        * strikethrough
* ***Color Patterns (expandable)***
    * rainbow
    * zebra

After chaining the various properties of your style, you may call the returned
object with text to obtain an ANSI wrapped version which is ready for printing.

An example of red text on a white background in bold would be:

``` python
print(paint.red.on_white.bold('Hello world!'))
```

An example of a blue zebra effect would be:

``` python
print(paint.zebra.blue('Look, a blue zebra!'))
```

Multiple arguments can be passed to the returned object which allows for
nesting of styles.

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
with the print function using the **sep** keyword argument.

``` python
print(paint('Hello', paint.cyan('there'), paint.green('buddy'), sep='_'))
```

#### Creating Custom Themes ####

You can easily create themes by saving a suitable instance of paint into a
variable and later calling it to invoke the saved style.

For example, let's create a style which provides bold red text on a magenta
background:

``` python
theme = paint.red.on_magenta.bold
```

Simply calling this variable with text from now on will render that style:

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
may verify your OS's color ability by importing the **supports_color**
function:

``` python
from painter import supports_color

if supports_color():
    print('Painter detected that your OS supports colors')
else:
    print('Painter detected that your OS does not support colors')
```

Painter will automatically enable or disable colors respectively if
**--color** or **--no-color** are included in the CLI arguments (sys.argv).

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

Furthermore, you can import the styles instance and use it directly without
going through the paint instance:

``` python
from painter import styles

print(styles.red.open + 'Some red text' + styles.red.close)
```

#### Lower-level Access to Patterns ####

Similarly to styles, you may access the callable required to generate any
pattern using the **patterns** member variable.

e.g.

``` python
print(paint.patterns.rainbow('Some red text'))
```

In this case, accessing the item directly doesn't really provide any useful
benefit over calling it directly from the paint instance.

However, you can import the patterns instance and use it directly without
going through the paint instance:

``` python
from painter import patterns

print(patterns.rainbow('Some red text'))
```

#### Stripping Color from Strings ####

You may also easily strip color from a string by importing and using the
**strip_color** function:

``` python
from painter import paint, strip_color

colored_text = paint.red.on_blue('Text with some color')
uncolored_text = strip_color(colored_text)
```

In addition to the strip_color function, Painter installs a basic CLI tool
named **strip-color** which can be used to strip color from text or a file.

To strip text from stdin, simply pipe it into the script:

``` bash
ls -l --color | strip-color > ls-without-colors.txt
```

To strip text from a file, ensure the filename follows the strip-color command:

``` bash
strip-color file-with-colors.txt > file-without-colors.txt
```

### Writing Custom Pattern Functions ###

Adding new pattern functions is extremely easy with Painter.  First, define a
function which takes in two parameters, the **text** and a **styles** object.
The function must return the processed text.

e.g. let's create a pattern which underlines every vowel

``` python
def underline_vowels(text, styles):
    vowel_text = ''
    for char in text:
        if char.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowel_text += styles.underline(char)
        else:
            vowel_text += char
    return vowel_text
```

To register this, simply run the **register** member function of the
**patterns** member variable.  This function takes two arguments, the **name**
of your pattern and your **function**.

``` python
paint.patterns.register('voweler', underline_vowels)
```

Now go ahead and use it immediately:

``` python
print(paint.voweler('I like puppies!'))
```

You may de-register a custom pattern at any time using the deregister function:

``` python
paint.patterns.deregister('voweler')
```

If you have imported the **patterns** instance directly, then registration is
identical:

``` python
patterns.register('voweler', underline_vowels)
```

## Running Tests ##

You may run the unit tests as follows:

``` bash
git clone https://github.com/fgimian/painter.git
cd painter
python setup.py test
```

You may validate Flake8 compatibility as follows:

``` bash
python setup.py flake8
```

## License ##

Painter is released under the **MIT** license. Please see the
[LICENSE](https://github.com/fgimian/painter/blob/master/LICENSE) file for
more details.

## Changelog ##

*You can click a version name to see a diff with the previous one.*

* ***[0.3.2-dev](https://github.com/fgimian/painter/compare/v0.3.1...master) (TBA)***
* ***[0.3.1](https://github.com/fgimian/painter/compare/v0.3...v0.3.1) (2014-04-29)***
    * Made strip-color CLI script more robust when errors occur
* ***[0.3](https://github.com/fgimian/painter/compare/v0.2...v0.3) (2014-04-28)***
    * Implemented coloring support for Windows using the colorama library.
    * Updated the test command to be run from setup.py to avoid unnecessary
      download of test dependencies during installation.
    * Renamed several of the utility functions for better consistency.  The
      paint API is unaffected by these changes.
    * The has_color variable is renamed to supports_color and should now be
      used as a function.
    * Implemented color patterns which generate varying color patterns on
      strings.  The rainbow and zebra patterns come included.
    * Custom pattern functions may now be written and easily registered with
      Painter.
    * Several bug fixes.
* ***0.2 (2014-04-26)***
    * Initial release
