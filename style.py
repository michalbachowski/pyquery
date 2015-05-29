# encoding: utf-8

class Style(object):

    def __init__(self, newline, indent):
        self.newline = str(newline)
        self.indent = str(indent)

class Pretty(Style):

    def __init__(self):
        super(Pretty, self).__init__("\n", '    ')

class Sparse(Style):

    def __init__(self):
        super(Sparse, self).__init__('', '')

