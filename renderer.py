# encoding: utf-8
from __future__ import absolute_import

from .dialects import Dialect
from .elements import Renderable
from .style import Style

class Renderer(object):
    """ Class that writes Renderable objects into predefined stream """

    """
    :type stream: file
    :type dialect: pyquery.dialects.Dialect
    :type style: pyquery.style.Style
    """

    def __init__(self, stream, style, dialect, indentation_level=0):
        """ Object initialization

        :param stream: stream to write values into
        :type stream: file
        :param style: style of rendered query
        :type style: pyquery.style.Style
        :param dialect: dialect used to render query
        :type dialect: pyquery.dialects.Dialect
        :param indentation_level: indentation level to be used by renderer
        :type indentation_level: int
        """
        assert isinstance(style, Style), 'style have to be subclass of Style'
        assert isinstance(dialect, Dialect), 'dialect have to be subclass of Dialect'

        self.stream = stream
        self.style = style
        self.dialect = dialect
        self.indentation_level = indentation_level

    def write(self, value, right=False):
        """ Writes given value into predefined stream

        :param value: value to be written. If instance of Renderable is given
            'render' method will be called. Otherwise value will be casted to str
        :type value: Renderable | type
        :param right: indicates that current object is placed on right hand side of and expression
        :type right: bool
        """
        if isinstance(value, Renderable):
            self.write(value.render(self, right))
        else:
            self.stream.write(str(value))
        return self

    def indent(self):
        """ Returns new renderer with increased indentation

        :returns: new instance of Renderer class with indentation_level increased
        :rtype: Renderer
        """
        return self.__class__(self.stream, self.style, self.dialect,
                              self.indentation_level + 1)

