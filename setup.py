"""
Painter
-------

.. image:: https://travis-ci.org/fgimian/painter.png?branch=v0.2
    :target: https://travis-ci.org/fgimian/painter
    :alt: Build Status
.. image:: https://coveralls.io/repos/fgimian/painter/badge.png?branch=master
    :target: https://coveralls.io/r/fgimian/painter?branch=master
    :alt: Coverage Status
.. image:: https://pypip.in/license/painter/badge.png
    :target: https://pypi.python.org/pypi/painter/
    :alt: License
.. image:: https://pypip.in/version/painter/badge.png
    :target: https://pypi.python.org/pypi/painter/
    :alt: Latest Version
.. image:: https://pypip.in/download/painter/badge.png
    :target: https://pypi.python.org/pypi/painter/
    :alt: Downloads

.. |logo| image:: https://raw.githubusercontent.com/fgimian/painter/master/images/painter_logo.png
    :alt: Painter Logo

|logo|

Painter is an ANSI coloring library based on the excellent
`chalk <https://github.com/sindresorhus/chalk>`_ and
`colors.js <https://github.com/marak/colors.js/>`_
libraries for Node.js.  However, painter attempts to provide an even more
expressive API which reads like English.

Painter is fully tested with 100% coverage and also completely Flake8
compliant too!

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

The output of this script looks something like this:

.. image:: https://raw.githubusercontent.com/fgimian/painter/master/images/painter_demo.png
    :alt: Painter Demo

Documentation
`````````````

For full details on using Painter, please check out the
`Painter GitHub Page <https://github.com/fgimian/painter>`_.

"""
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


# Inspired by the example at https://pytest.org/latest/goodpractises.html
class NoseTestCommand(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # Run the nose ensuring that argv simulates running nosetests directly
        import nose
        nose.run_exit(argv=['nosetests'])

# Colorama is needed on Windows to enable ANSI coloring
install_requires = []
if sys.platform == 'win32':
    install_requires.append('colorama')

setup(
    name='painter',
    version='0.3.1',
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
            'strip-color = painter.strip_color_cli:main'
        ]
    },
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[
        'nose',
        'coverage',
        'mock'
    ],
    setup_requires=[
        'flake8'
    ],
    cmdclass={'test': NoseTestCommand},
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
    ]
)
