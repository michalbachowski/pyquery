# encoding: utf-8

class Style(object):

    def __init__(self, newline, indent):
        self.indent = str(indent)
        self.newline = str(newline)

def pretty():
    return Style("\n", '    ')

def sparse():
    return Style('', ' ')
