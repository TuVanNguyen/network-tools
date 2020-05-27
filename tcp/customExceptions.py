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

class QuitServer(Exception):
    """
    Exception raised when you want to quit server
    """

    def __init__(self, host,port):
        self.host = host
        self.port = port

    def __str__(self):
        return "'Quitting server listening on {0}:{1}".format(self.host,self.port)


        

