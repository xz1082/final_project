"""
Creator: Sylvia Zhao

Contributor: Wenxi Lei, Tian Wang
"""

class CannotRead(Exception):
    def __str__(self):
        return "Cannot read file. Please input name of file with .csv extension."

class MissingHeader(Exception):
    def __str__(self):
        return "Missing headers in local file. Please make sure column headers for data include: Open, High, Low, Close, Volume"

class UserEmptyString(Exception):
    def __str__(self):
        return "Empty string detected. Please input: Start Date, and End Date."