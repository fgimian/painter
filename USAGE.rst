Usage
-----

The Painter
~~~~~~~~~~~

Start by importing your painter as follows:

.. code:: python

    from painter import paint

Generating Colored Text
^^^^^^^^^^^^^^^^^^^^^^^

You may now use the **paint** instance for all your painting needs.
Simply chain any combination of a foreground color, a background color,
style modifiers and color patterns.

The following are available:

- **Foreground colors**
    - Standard colors most commonly supported
        - black
        - red
        - green
        - yellow
        - blue
        - magenta
        - cyan
        - white
    - Extended colors for systems supporting up to 16 colors
        - light_black (or gray / grey)
        - light_red
        - light_green
        - light_yellow
        - light_blue
        - light_magenta
        - light_cyan
        - light_white
- **Background colors**
    - Standard colors most commonly supported
        - on_black
        - on_red
        - on_green
        - on_yellow
        - on_blue
        - on_magenta
        - on_cyan
        - on_white
    - Extended colors for systems supporting up to 16 colors
        - on_light_black (or on_gray / on_grey)
        - on_light_red
        - on_light_green
        - on_light_yellow
        - on_light_blue
        - on_light_magenta
        - on_light_cyan
        - on_light_white
- **Style Modifiers**
    - Styles most commonly supported
        - reset
        - bold
        - underline
        - blinking
        - inverse
    - Not widely supported
        - faint
        - italic
        - invisible
        - strikethrough
- **Color Patterns (expandable)**
    - rainbow
    - zebra

After chaining the various properties of your style, you may call the
returned object with text to obtain an ANSI wrapped version which is
ready for printing.

An example of red text on a white background in bold would be:

.. code:: python

    print(paint.red.on_white.bold('Hello world!'))

An example of a blue zebra effect would be:

.. code:: python

    print(paint.zebra.blue('Look, a blue zebra!'))

Multiple arguments can be passed to the returned object which allows for
nesting of styles.

For example, let's print various text colors on a red background:

.. code:: python

    print(paint.on_red('Unstyled', paint.blue('blue'), paint.green('green'),
                       paint.bold('regular color and bold')))

Naturally, you can nest any styles you want. For example, you can start
with bold text and vary the color of various words.

.. code:: python

    print(paint.bold('Regular bold', paint.blue('blue'),
                     paint.on_red('red background')))

Multiple arguments passed to the paint callable will be separated by a
single white space. However, you can customise this similarly to the way
you do with the print function using the **sep** keyword argument.

.. code:: python

    print(paint('Hello', paint.cyan('there'), paint.green('buddy'), sep='_'))

Creating Custom Themes
^^^^^^^^^^^^^^^^^^^^^^

You can easily create themes by saving a suitable instance of paint into
a variable and later calling it to invoke the saved style.

For example, let's create a style which provides bold red text on a
magenta background:

.. code:: python

    theme = paint.red.on_magenta.bold

Simply calling this variable with text from now on will render that
style:

.. code:: python

    print(theme('My special little theme'))

Just like regular styles, themes can also be nested:

.. code:: python

    theme_bg = paint.on_white
    theme_text_a = paint.red.bold
    theme_text_b = paint.blue.underline
    print(theme_bg(theme_text_a('Hello'), theme_text_b('world!')))

Color Support & Enabling or Disabling Colors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, Painter will attempt to detect if your OS supports colors.
You may verify your OS's color ability by importing the
**supports_color** function:

.. code:: python

    from painter import supports_color

    if supports_color():
        print('Painter detected that your OS supports colors')
    else:
        print('Painter detected that your OS does not support colors')

Painter will automatically enable or disable colors respectively if
**--color** or **--no-color** are included in the CLI arguments
(sys.argv).

However, if you would like to explicitly enable or disable coloring,
simply update the boolean member variable **enabled**.

e.g.

.. code:: python

    paint.enabled = False

Color Utilities
~~~~~~~~~~~~~~~

Lower-level Access to Styles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may access the open and close string required to print any color or
style using the **styles** member variable.

e.g.

.. code:: python

    print(paint.styles.red.open + 'Some red text' + paint.styles.red.close)

Furthermore, you can import the styles instance and use it directly
without going through the paint instance:

.. code:: python

    from painter import styles

    print(styles.red.open + 'Some red text' + styles.red.close)

Lower-level Access to Patterns
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Similarly to styles, you may access the callable required to generate
any pattern using the **patterns** member variable.

e.g.

.. code:: python

    print(paint.patterns.rainbow('Some red text'))

In this case, accessing the item directly doesn't really provide any
useful benefit over calling it directly from the paint instance.

However, you can import the patterns instance and use it directly
without going through the paint instance:

.. code:: python

    from painter import patterns

    print(patterns.rainbow('Some red text'))

Stripping Color from Strings
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You may also easily strip color from a string by importing and using the
**strip_color** function:

.. code:: python

    from painter import paint, strip_color

    colored_text = paint.red.on_blue('Text with some color')
    uncolored_text = strip_color(colored_text)

In addition to the strip_color function, Painter installs a basic CLI
tool named **strip-color** which can be used to strip color from text or
a file.

To strip text from stdin, simply pipe it into the script:

.. code:: bash

    ls -l --color | strip-color > ls-without-colors.txt

To strip text from a file, ensure the filename follows the strip-color
command:

.. code:: bash

    strip-color file-with-colors.txt > file-without-colors.txt

Writing Custom Pattern Functions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adding new pattern functions is extremely easy with Painter. First,
define a function which takes in two parameters, the **text** and a
**styles** object. The function must return the processed text.

e.g. let's create a pattern which underlines every vowel

.. code:: python

    def underline_vowels(text, styles):
        vowel_text = ''
        for char in text:
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowel_text += styles.underline(char)
            else:
                vowel_text += char
        return vowel_text

To register this, simply run the **register** member function of the
**patterns** member variable. This function takes two arguments, the
**name** of your pattern and your **function**.

.. code:: python

    paint.patterns.register('voweler', underline_vowels)

Now go ahead and use it immediately:

.. code:: python

    print(paint.voweler('I like puppies!'))

You may de-register a custom pattern at any time using the deregister
function:

.. code:: python

    paint.patterns.deregister('voweler')

If you have imported the **patterns** instance directly, then
registration is identical:

.. code:: python

    patterns.register('voweler', underline_vowels)
