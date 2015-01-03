from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import codecs
import os
import sys
import re

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()

def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long', 'test']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='binplist',
    version=find_version('binplist', '__init__.py'),
    url='https://github.com/provegard/binplist',
    license='BSD',
    author='Per Rovegard',
    tests_require=['pytest'],
    install_requires=['click'],
    cmdclass={'test': PyTest},
    author_email='per@rovegard.se',
    description='Reads Apple binary plist files',
    long_description='Provides an API and a CLI for reading Apply binary plist files, Python 2 & 3 compatibility.',
    keywords='binary plist',
    entry_points={
        'console_scripts': [
            'binplist-cli = binplist.cli:run',
            ],
        },
    packages=['binplist'],
    include_package_data=True,
    platforms='any',
    test_suite='binplist.test.test_plist',
    zip_safe=False,
    package_data={},
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    extras_require={
        'testing': ['pytest'],
      }
)
