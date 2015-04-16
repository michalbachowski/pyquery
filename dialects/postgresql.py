# encoding: utf-8

from __future__ import absolute_import

from . import Dialect
from ..elements.structural import AbstractLimit
from ..elements.text import Newline, Indentation

class _Limit(AbstractLimit):

    def render(self, renderer, right=False):
        renderer.write(Indentation())\
            .write('limit ')\
            .write(self.limit, True)\
            .write(Newline())
        if self.offset:
            renderer.write(Indentation())\
                .write('offset ')\
                .write(self.offset, True)\
                .write(Newline())


PostgreSQL = Dialect([], "'", '"')
