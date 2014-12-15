'''
Created on 2014.12.1

@author: Fangyun Sun
'''


import requests
from Utilities.Exceptions import *

def IsInternetOn():
    """
    Check whether the internet is connected. We need to obtain data from yahoo finance through the Internet.
    We use the google website for default options.
    If we cannot connect the internet, raise ConnectInternetException.
    """
    try:
        _ = requests.get('http://www.google.com/', timeout=5)
        return True
    except requests.ConnectionError: 
        raise ConnectInternetException()
    return False

if __name__ == '__main__':
    print IsInternetOn()