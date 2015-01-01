binplist
========

Python module for reading an Apple binary plist. When I wrote this code, the Python standard
library didn't have support for reading binary plists.

What's the point of it now, given that Python 3 has binary plist support? Two reasons:

* Python 2 doesn't support it.
* In my testing, the plist implementation in Python 3.4.2 fails to read some binary plist
  files present in iPhone backups.

Author & contact
----------------
Per Rovegård

E-mail: per@rovegard.se

Twitter: @provegard

Blog: http://programmaticallyspeaking.com

License
-------

binplist is licensed under the 3-clause BSD license. See the LICENSE file for the full license text.
