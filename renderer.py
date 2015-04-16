# encoding: utf-8
from __future__ import absolute_import

import abc
from ._compat import with_metaclass


def iseparate(separator, iterable):
    try:
        yield next(iterable)
        while True:
            val = next(iterable)
            yield separator
            yield val
    except StopIteration:
        return

def render_list(values, renderer, level, right=False):
    for value in values:
        value.render(renderer, level, right)

class Renderer(object):

    def __init__(self, stream, style, dialect, indentation_level=0):
        self.stream = stream
        self.style = style
        self.dialect = dialect
        self.indentation_level = indentation_level

    def write(self, value, right=False):
        if hasattr(value, 'render'):
            self.write(value.render(self, right=False))
        else:
            self.stream.write(value)
        return self

    def indent(self):
        return self.__class__(self.stream, self.style, self.dialect,
                              self.indentation_level + 1)

class Renderable(with_metaclass(abc.ABCMeta)):

    @abc.abstractmethod
    def render(self, renderer, right=False):
        """

        :param right: is element right-associative
        """
        pass
