"""
Creator: Sylvia Zhao

Contributor: Wenxi Lei, Tian Wang
"""

class EmptyString(Exception):
    def __str__(self):
        return ("Empty string detected. Please input: Symbol, Source, Start Date, and End Date.")
    pass

class BadSource(Exception):
    def __str__(self):
        return "Bad source. Please input 'yahoo' or 'google' into Source."
    pass

class BadTicker(Exception):
    def __str__(self):
        return "Bad ticker. Data not available for given stock for specified start and end dates. Please input valid Ticker Symbol and valid corresponding Start / End Dates."

class BadDate(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return repr(self.msg)
