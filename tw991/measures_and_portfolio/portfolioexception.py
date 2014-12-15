"""
Creator: Tian Wang

Contributor: Wenxi Lei, Sylvia Zhao
"""


class Invalidposition(Exception):
    """
    Raised when input position is not valid
    """
    def __str__(self):
        return "Input position is invalid!"
    pass


class Undefinedposition(Exception):
    """
    Raised if simulate() function is called when position is not defined.
    """
    def __str__(self):
        return "Undefined position!"
    pass


class Invaliddatetimeinput(Exception):
    """
    Raised when datetime input is invalid
    """
    def __str__(self):
        return "Invalid datetime input!"
    pass

class InvalidTickerlist(Exception):
    """
    Raised when ticker_list input for portfolio class is not list
    """
    def __str__(self):
        return "Invalid ticker list input! It needs to be a list!"