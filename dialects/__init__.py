# encoding: utf-8

class Dialect(object):

    def __init__(self, priorities, value_quote, field_quote,
                 value_separator, limit_class, types):
        self.priorities = priorities
        self.value_quote = value_quote
        self.field_quote = field_quote
        self.value_separator = value_separator
        self.limit_class = limit_class
        self.types = types

