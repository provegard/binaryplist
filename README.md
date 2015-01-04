binaryplist
===========

[![Build Status](https://travis-ci.org/provegard/binaryplist.svg?branch=master)](https://travis-ci.org/provegard/binaryplist)

Python module for reading an Apple binary plist. When I wrote this code back in 2011 as part
of another project, the Python standard library didn't have support for reading binary plists.
Python 2 still hasn't, whereas support has been added in Python 3.

What's the point of it now then, given that Python 3 has binary plist support? Two reasons:

* Python 2 compatibility.
* In my testing, the plist implementation in Python 3.4.2 fails to read some binary plist
  files present in iPhone backups.

Usage
-----

The module exposes a single function:

    read_binary_plist(fd)

`fd` is a file descriptor opened for reading in binary mode. The file must support
seeking.

The return value is the root object of the plist file.

The function raises `PListFormatError` if the file does not have the expected format.
It raises `PListUnhandledError` if the file contains an unsupported feature.

Command-line interface
----------------------

The module installs a script that can be used from the command-line. The basic usage
of the script is:

    binaryplist-cli [--format=<json|plist>] <filename>

Where:

* `--format` selects output format. By default, the plist is printed on standard output
  using XML plist format. Alternatively, you may request JSON to be used instead.
* `filename` refers to a path of an existing binary plist file.

Installing
----------

*binaryplist* can be installed directly from GitHub using pip:

    pip install git+git://github.com/provegard/binaryplist.git

Or from PyPi:

    pip install binaryplist

Use `pip3` for a Python 3 installation. The `https` scheme can also be used.

Compatibility
-------------

Tested with Python 2.7 and 3.4 using `tox`. Python 2.6 not tested due to this issue:
https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=754248

Related
-------

The Python 3 `plistlib` module: https://docs.python.org/3/library/plistlib.html

Python 3.4.2 doesn't support set data and parses date into local `datetime` objects,
whereas this module returns UTC `datetime` objects.

`binplist`: https://code.google.com/p/binplist

`binplist` parses set data into an array, whereas `binaryplist` (this module) parses
it into a Python `set`.


Author & contact
----------------
Per Roveg&aring;rd

E-mail: per@rovegard.se

Twitter: @provegard

Blog: http://programmaticallyspeaking.com

License
-------

*binaryplist* is licensed under the 3-clause BSD license. See the LICENSE file for the full license text.
