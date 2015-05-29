# encoding: utf-8
from __future__ import absolute_import

def iseparate(separator, iterable):
    """ Returns generator that separates given iterable with given separator.
    Works similarily to str.join which means that separator is never lest at the end

    >>> list(iseparate(',', [1,2,3]))
    [1, ',', 2, ',', 3]

    :param separator: value to separate elements of iterable with
    :type separator: type
    :param iterable: iterable containing elements to separate
    :type iterable: iterable
    :returns: generator
    :rtype: iterable
    """
    try:
        yield next(iterable)
        while True:
            val = next(iterable)
            yield separator
            yield val
    except StopIteration:
        return

