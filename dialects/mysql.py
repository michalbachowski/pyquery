# encoding: utf-8

from __future__ import absolute_import

from . import Dialect
from ..elements.structural import Select, From, Join, Where, Order, Limit

MySQL = Dialect([Select, From, Join, Where, Order, Limit], '"', '`')
