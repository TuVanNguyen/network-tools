class Error(Exception):
    pass

class PortValueError(Error):
    """
    Exception raised if port value is invalid
    """

    def __init__(self, expression, value):
        self.expression = expression
        self.value = value

    def __str__(self):
        return "'{}' is an invalid port number".format(self.value)
