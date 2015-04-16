# encoding: utf-8

class Dialect(object):

    def __init__(self, template, value_quote, field_quote):
        self.template = template
        self.value_quote = value_quote
        self.field_quote = field_quote

