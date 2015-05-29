# encoding: utf-8

from __future__ import absolute_import

from . import Dialect
from . import SQL92
from ..elements import Literal
from ..elements.text import Newline, Indentation

class Limit(Literal):

    def render(self, renderer, right=False):
        renderer.write(Indentation())\
            .write('limit ')\
            .write(self.value.limit, True)\
            .write(Newline())
        if self.offset:
            renderer.write(Indentation())\
                .write('offset ')\
                .write(self.value.offset, True)\
                .write(Newline())

class PostgreSQL(Dialect):

    def __init__(self):
        sql92 = SQL92()
        super(PostgreSQL, self).__init__(
            sql92.priorities, "'", '"',
            sql92.value_separator, Limit, {'ip': 'inet'}
        )

