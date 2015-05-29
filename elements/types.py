# encoding: utf-8

from . import Literal, Quoted, Aggregated
from .structural import Keyword
from .._compat import (map, string_types, integer_types, ip_types)
from ..renderer import Renderable

def native(value):

    if value is None:
        return Null()

    if isinstance(value, integer_types):
        return Literal(value)

    if ip_types and isinstance(value, ip_types):
        return IP(value)

    if isinstance(value, string_types):
        return Quoted(value)

    if isinstance(value, (tuple, list, set, frozenset)):
        return Aggregated(map(native, value))

    raise TypeError('Could not discover value type for {!r}'.format(value))

class Null(Renderable):

    def render(self, renderer, right=False):
        renderer.write(renderer.dialect.types['null'])

class WithType(Quoted):

    TYPE_NAME = None

    def type_name(self, dialect):
        return Keyword(dialect.types[self.TYPE_NAME])

    def render(self, renderer, right=False):
        renderer.write('cast(', right)
        super(IP, self).render(renderer, False)
        renderer.write(' as ', False) \
                .write(self.type_name(renderer.dialect), False) \
            .write(')', False)

class IP(WithType):
    TYPE_NAME = 'ip'

