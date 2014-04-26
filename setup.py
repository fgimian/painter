"""
Painter
-------

Painter is an ANSI coloring library heavily based on the awesome
`chalk <https://github.com/sindresorhus/chalk>`_ library for Node.js along
with all its dependences.  However, painter attempts to provide an even more
expressive API which reads like English.

Painter is fully tested with 100% coverage and also completely Flake8
compilant too!

Quick Start
```````````

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

    # Chaining colors
    print(paint.blue.on_red.bold.underline('and far more complex combos too'))
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
"""
from setuptools import setup


setup(
    name='painter',
    version='0.2',
    url='https://github.com/fgimian/painter',
    license='MIT',
    author='Fotis Gimian',
    author_email='fgimiansoftware@gmail.com',
    description=(
        'Your own expressive painter who colors text in your terminal.'
    ),
    long_description=__doc__,
    packages=['painter'],
    entry_points={
        'console_scripts': [
            'strip_ansi = painter.strip_ansi_cli:main'
        ]
    },
    zip_safe=False,
    setup_requires=[
        'nose',
        'coverage',
        'mock',
        'flake8'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Terminals'
    ],
)
