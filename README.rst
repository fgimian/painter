Painter
=======

|Build Status| |Coverage Status| |License| |Latest Version|

.. |Build Status| image:: https://travis-ci.org/fgimian/painter.png?branch=master
   :target: https://travis-ci.org/fgimian/painter
.. |Coverage Status| image:: https://coveralls.io/repos/fgimian/painter/badge.svg
   :target: https://coveralls.io/r/fgimian/painter
.. |License| image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://github.com/fgimian/painter/blob/master/LICENSE
.. |Latest Version| image:: https://img.shields.io/pypi/v/painter.svg
   :target: https://pypi.python.org/pypi/painter/

.. image:: https://raw.githubusercontent.com/fgimian/painter/master/images/painter-logo.png
   :alt: Painter Logo

Awesome artwork provided courtesy of `Open Clip Art
Library <http://openclipart.org/detail/174634/painter-penguin-by-moini-174634>`_

Introduction
------------

Painter is an ANSI coloring library based on the excellent
`chalk <https://github.com/sindresorhus/chalk>`_ and
`colors.js <https://github.com/marak/colors.js/>`_ libraries for
Node.js. However, painter attempts to provide an even more expressive
API which reads like English.

Painter is fully tested with 100% coverage and also completely Flake8
compliant too!

Quick Start
-----------

Install Painter in your virtualenv as follows:

.. code:: bash

    pip install painter

And now, go ahead and use it to output colors to your terminal:

.. code:: python

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

The output of the script above looks something like this:

.. image:: https://raw.githubusercontent.com/fgimian/painter/master/images/painter-demo.png
   :alt: Painter Demo

Documentation
-------------

Please check out the `Painter Usage documentation
<https://github.com/fgimian/painter/blob/master/USAGE.rst/>`_.

Running Tests
-------------

You may run the unit tests as follows:

.. code:: bash

    git clone https://github.com/fgimian/painter.git
    cd painter
    python setup.py test

You may validate Flake8 compatibility as follows:

.. code:: bash

    python setup.py flake8

License
-------

Painter is released under the **MIT** license. Please see the
`LICENSE <https://github.com/fgimian/painter/blob/master/LICENSE>`_
file for more details.
