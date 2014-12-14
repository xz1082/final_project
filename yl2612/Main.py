'''
Created on 2014.12.9

@author: Fangyun Sun
'''

from Tkinter import *
import ttk
from WindowPackage.MainWindow import MainWindow


def main():
    root = Tk()
    root.title("Stock Analysis")
    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()