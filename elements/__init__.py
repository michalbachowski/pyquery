# encoding: utf-8
from __future__ import absolute_import

from ..renderer import Renderable

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
