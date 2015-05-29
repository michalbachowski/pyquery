# encoding: utf-8
from __future__ import absolute_import

import abc

from ._compat import with_metaclass
from .dialects import Dialect
from .style import Style

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

class Renderer(object):
    """ Class that writes Renderable objects into predefined stream """

    """
    :type stream: file
    :type dialect: pyquery.dialects.Dialect
    :type style: pyquery.style.Style
    """

    def __init__(self, stream, style, dialect, indentation_level=0):
        """ Object initialization

        :param stream: stream to write values into
        :type stream: file
        :param style: style of rendered query
        :type style: pyquery.style.Style
        :param dialect: dialect used to render query
        :type dialect: pyquery.dialects.Dialect
        :param indentation_level: indentation level to be used by renderer
        :type indentation_level: int
        """
        assert isinstance(style, Style), 'style have to be subclass of Style'
        assert isinstance(dialect, Dialect), 'dialect have to be subclass of Dialect'

        self.stream = stream
        self.style = style
        self.dialect = dialect
        self.indentation_level = indentation_level

    def write(self, value, right=False):
        """ Writes given value into predefined stream

        :param value: value to be written. If instance of Renderable is given
            'render' method will be called. Otherwise value will be casted to str
        :type value: Renderable | type
        :param right: indicates that current object is placed on right hand side of and expression
        :type right: bool
        """
        if isinstance(value, Renderable):
            self.write(value.render(self, right))
        else:
            self.stream.write(str(value))
        return self

    def indent(self):
        """ Returns new renderer with increased indentation

        :returns: new instance of Renderer class with indentation_level increased
        :rtype: Renderer
        """
        return self.__class__(self.stream, self.style, self.dialect,
                              self.indentation_level + 1)

class Renderable(with_metaclass(abc.ABCMeta)):
    """ Base class for renderable value objects """

    @abc.abstractmethod
    def render(self, renderer, right=False):
        """ Renders current value object

        :param renderer: renderer to be used to render value of object
        :type renderer: Renderer
        :param right: indicates that current object is placed on right hand side of and expression
        :type right: bool
        """
        pass # pragma: no cover

