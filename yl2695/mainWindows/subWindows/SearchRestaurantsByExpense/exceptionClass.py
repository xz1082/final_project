# author: Wenying Liu(wl1207) and Yucheng Lu(yl2695)

class stateInputError(Exception):
    
	"""
    This exception will raise when user input for state does not follow the instruction.
    """
    
	pass
	
class priceInputError(Exception):
    
	"""
    This exception will raise when user input for price does not follow the instruction.
    """
    
	pass
	
class num_topInputError(Exception):
    
	"""
    This exception will raise when user input for num_top does not follow the instruction.
    """
    
	pass

class noneDataFrameError(Exception):
    '''
    This exeption will raise when the dataframe user searches is none.
    '''

    pass