# encoding: utf-8

from __future__ import absolute_import

from . import Dialect
from .sql92 import SQL92
from ..elements import Literal
from ..elements.text import Indentation

class Limit(Literal):

    def render(self, renderer, right=False):
        renderer.write(Indentation())
        renderer.write('limit ')
        if self.offset:
            renderer.write(self.value.offset, True)
            renderer.write(',', True)
        renderer.write(self.value.limit, True)

class MySQL(Dialect):

    def __init__(self):
        sql92 = SQL92()
        super(MySQL, self).__init__(
            sql92.priorities, '"', '`',
            sql92.value_separator, Limit, {}
        )

