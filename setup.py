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

# Read the long description from readme.rst
with open('setup.rst') as f:
    long_description = f.read()


setup(
    name='painter',
    version='0.3.2.dev0',
    url='https://github.com/fgimian/painter',
    license='MIT',
    author='Fotis Gimian',
    author_email='fgimiansoftware@gmail.com',
    description=(
        'Your own expressive painter who colors text in your terminal.'
    ),
    long_description=long_description,
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
