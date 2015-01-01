binplist
========

Python module for reading an Apple binary plist. When I wrote this code, the Python standard
library didn't have support for reading binary plists.

What's the point of it now, given that Python 3 has binary plist support? Two reasons:

* Python 2 doesn't support it.
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

    binplist-cli [--format=&lt;json|plist&gt;] <filename>

Where:

* `--format` selects output format. By default, the plist is printed on standard output
  using XML plist format. Alternatively, you may request JSON to be used instead.
* `filename` refers to a path of an existing binary plist file.

Installing
----------

*binplist* can be installed directly from GitHub using pip:

    pip install git+git://github.com/provegard/binplist.git

The `https` scheme can also be used.

Author & contact
----------------
Per Rovegård

E-mail: per@rovegard.se

Twitter: @provegard

Blog: http://programmaticallyspeaking.com

License
-------

*binplist* is licensed under the 3-clause BSD license. See the LICENSE file for the full license text.
