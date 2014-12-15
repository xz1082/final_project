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
    
class Emptydf(Exception):
    def __str__(self):
        return "Dataframe is empty."
    
class Baddtype(Exception):
    def __str__(self):
        return "Bad dtype. Please make sure first column is in datetime format yyyy/mm/dd and data for all other columns are float64."
