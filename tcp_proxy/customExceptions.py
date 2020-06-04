#!/usr/bin/env python

class PortValueError(Exception):
    """
        Exception raised if port value is invalid
    """

    def __init__(self, expression, value):
        self.expression = expression
        self.value = value

    def __str__(self):
        return "'{0}' is an invalid port number for {1}".format(self.value,self.expression)

class ArgumentNumberError(Exception):
    """
    Exception raised if number of arguments not right
    """
    def __init__(self,usage, example):
        self.usage = usage
        self.example = example
    def __str__(self):
        return "{0}\n{1}".format(self.usage,self.example)

class BooleanValueError(Exception):
    """
    Exception raised if boolean value
    """
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return "'{}' is not a valid boolean value. Please enter true/false".format(self.value)
