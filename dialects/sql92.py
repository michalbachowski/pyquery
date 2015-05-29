# encoding: utf-8

from __future__ import absolute_import

from . import Dialect
from ..elements import Literal
from ..elements.text import Indentation


class Limit(Literal):
    pass

class SQL92(Dialect):

    def __init__(self):
        super(SQL92, self).__init__(
            ['select', 'from', 'join', 'where', 'order', 'limit'],
            "'", '', ',', Limit, {}
        )

