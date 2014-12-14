# -*- coding: utf-8 -*-
"""
Created on Tue Dec  9 17:15:15 2014

@author: peter
"""

import Tkinter,tkFileDialog

def getFileLocation(msg):
    
    root = Tkinter.Tk()
    root.withdraw()
    
    filePath = tkFileDialog.askopenfilename(initialdir="./",title = msg)   
    
    return filePath
    
    