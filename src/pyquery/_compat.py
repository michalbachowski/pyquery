# -*- coding: utf-8 -*-
"""
Python 2.7.x, 3.2+ compatability module.
"""
from __future__ import (absolute_import, unicode_literals, print_function, division)
import operator
import sys

is_py2 = sys.version_info[0] == 2

def with_metaclass(meta, *bases):
    """Create a base class with a metaclass.
    Taken from python's "six" package source code:

    http://pythonhosted.org/six/#six.with_metaclass
    """
    # This requires a bit of explanation: the basic idea is to make a dummy
    # metaclass for one level of class instantiation that replaces itself with
    # the actual metaclass.
    class metaclass(meta):

        def __new__(cls, name, this_bases, d):
            return meta(name, bases, d)
    return type.__new__(metaclass, b'temporary_class', (), {})

if not is_py2:
    # Python 3

    # strings and ints
    text_type = str
    string_types = (str,)
    integer_types = (int,)
    basestring = str

    # lazy iterators
    filter = filter
    from itertools import filterfalse
    map = map
    range = range
    zip = zip
    iteritems = operator.methodcaller(b'items')
    iterkeys = operator.methodcaller(b'keys')
    itervalues = operator.methodcaller(b'values')

    # other
    import ipaddress
    ip_parser = ipaddress.ip_address
    ip_types = (ipaddress.IPv4Address, ipaddress.IPv6Address)

else:
    # Python 2

    # strings and ints
    text_type = unicode
    string_types = (str, unicode)
    integer_types = (int, long)
    basestring = basestring

    # lazy iterators
    from itertools import (ifilter, ifilterfalse, imap, izip)
    filter = ifilter
    filterfalse = ifilterfalse
    map = imap
    range = xrange
    zip = izip
    iteritems = operator.methodcaller(b'iteritems')
    iterkeys = operator.methodcaller(b'iterkeys')
    itervalues = operator.methodcaller(b'itervalues')

    # other
    ip_parser = str
    ip_types = None
