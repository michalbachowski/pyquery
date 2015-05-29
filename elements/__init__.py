# encoding: utf-8
from __future__ import absolute_import

import abc

from ._compat import with_metaclass

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

class Literal(Renderable):

    def __init__(self, value):
        self.value = str(value)

    def render(self, renderer, right=False):
        renderer.write(self.value)

class Aggregated(Renderable):

    def __init__(self, value):
        self.value = list(value)

    def render(self, renderer, right=False):
        for value in self.value:
            renderer.write(value, right)

class Quoted(Literal):

    def render(self, renderer, right=False):
        renderer.write(renderer.dialect.value_quote)\
                .write(self.value)\
                .write(renderer.dialect.value_quote)

class Field(Literal):

    def render(self, renderer, right=False):
        renderer.write(renderer.dialect.field_quote)\
                .write(self.value)\
                .write(renderer.dialect.field_quote)
