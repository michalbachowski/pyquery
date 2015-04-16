# encoding: utf-8
from __future__ import absolute_import

from ..renderer import Renderable

class Newline(Renderable):

    def render(self, renderer, right=False):
        renderer.write(renderer.style.newline)

class Indentation(Renderable):

    def render(self, renderer, right=False):
        renderer.write(renderer.style.indent * renderer.indentation_level)

