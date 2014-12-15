"""
Creator: Tian Wang

Contributor: Wenxi Lei, Sylvia Zhao
"""

class Invalidperiodlength(Exception):
    """
    Raised when moving average computation length is smaller than length of data
    """
    def __str__(self):
        return "Input length is invalid!"
    pass


class InvalidinputData(Exception):
    """
    Raised when input data is not valid
    """
    def __str__(self):
        return "Input data is invalid!"
    pass


class MultipleCol(Exception):
    """
    Raised when data with multiple columns is input
    """
    def __str__(self):
        return "Multiple columns! Require only 1!"
    pass


class BollinvalidN(Exception):
    """
    Raised when moving average N for boll(series, N, K) is not a valid positive integer
    """
    def __str__(self):
        return "Invalid N input for Bollinger Band! Must be positive integer!"
    pass


class BollinvalidK(Exception):
    """
    Raised when standard deviation factor K for boll(series, N, K) is not a positive number
    """
    def __str__(self):
        return "Invalid K input for Bollinger Band! Must be positive number!"
    pass


class Macdinvalidperiod(Exception):
    """
    Raised when fast period is larger than slow period in macd(series, slow, fast)
    """
    def __str__(self):
        return "Invalid period setting for macd!"
    pass


class Negativevalue(Exception):
    """
    Raised when there is at least 1 negative value in the data
    """
    def __str__(self):
        return "Can't take negative values!"
    pass