# encoding: utf-8
from __future__ import absolute_import

from . import Aggregated, Literal, Field
from .text import Newline, Indentation
from ..renderer import Renderable, render_list, iseparate

__all__ = ['Select', 'From', 'Join', 'Where', 'Order', 'Limit', 'Keyword']

class Keyword(Literal):

    def render(self, renderer, right=False):
        renderer.write(Indentation()).write(self.value.upper())

class MultiValue(Renderable):

    separator = ','

    required = False

    name = None

    def __init__(self, *args):
        self._values = args

    def field_name(self):
        return self.name

    def render(self, renderer, right=False):
        if self.required and len(self._values) == 0:
            raise ValueError('Value for "{}" part is required'.format(
                self.name
            ))

        renderer.write(Field(self.field_name)).write(Newline())
        self._render(renderer)
        renderer.write(Newline())

    def _render(self, renderer, right=False):
        render_list(iseparate(Aggregated(self.separator, Newline()), self._values),
                    renderer.indent())

class SingleValue(MultiValue):

    def render(self, renderer, right=False):
        if len(self._values) > 1:
            raise ValueError('Expected single value, but {} values found'.format(len(self._values)))

        super(SingleValue, self).render(renderer, right)

    def _render(self, renderer, right=False):
        renderer.indent().write(self._values[0])

class Select(MultiValue):

    required = True
    name = 'select'

class From(MultiValue):
    name = 'from'

class Join(MultiValue):
    name = 'join'

class Where(SingleValue):
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

