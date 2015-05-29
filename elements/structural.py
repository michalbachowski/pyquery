# encoding: utf-8
from __future__ import absolute_import

from . import Aggregated, Literal, Field
from .text import Newline, Indentation, ValueSeparator
from ..renderer import Renderable, iseparate

__all__ = ['Select', 'From', 'Join', 'Where', 'Order', 'Limit', 'Keyword']

class Keyword(Literal):

    def render(self, renderer, right=False):
        renderer.write(Indentation()).write(self.value.upper())

class MultiValue(Aggregated):

    required = False

    name = None

    def __init__(self, *args):
        super(MultiValue, self).__init__(
            iseparate(
                Aggregated([ValueSeparator(), Newline()]),
                args
            )
        )

    def render(self, renderer, right=False):
        if self.required and len(self._values) == 0:
            raise ValueError('Value for "{}" part is required'.format(
                self.name
            ))

        renderer.write(Field(self.name)).write(Newline())
        super(MultiValue, self).render(renderer.indent())
        renderer.write(Newline())

class Select(MultiValue):
    required = True
    name = 'select'

class From(MultiValue):
    name = 'from'

class Join(MultiValue):
    name = 'join'

class Where(Renderable):
    name = 'where'

class Order(MultiValue):
    name = 'order'

class Limit(Renderable):
    name = 'limit'

    def __init__(self, limit, offset=0):
        self.limit = limit
        self.offset = offset

    def render(self, renderer, right=False):
        renderer.dialect.limit_class(self).render(renderer, right)

