"""
Creator: Wenxi Lei

Contributor: Sylvia Zhao, Tian Wang
"""

from Tkinter import *
from tkFileDialog import askopenfilename

import matplotlib.pyplot as plt
from matplotlib.widgets import RadioButtons
from matplotlib.widgets import Cursor
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

import numpy as np
import pandas as pd

from plot.plot import plot_stock
from data_process.retrieve_data import get_data
from measures_and_portfolio.stock_class import stock
from measures_and_portfolio.portfolio import portfolio
from data_process.userfile import userfile_read

instruction="""Brief Instruction:
1. Basic Summary and Interactive Graphics
1.1 Enter the stock ticker symbol, web source(CASE SENSITIVE: yahoo, google),\nstart and end date in yyyy/mm/dd format if you choose not to use local file.
1.2 Press 'Show Numerical Statistics' to print the numerical statistics during this period
1.3 Press 'Show Summary' to print the mean, standard deviation etc. during this period
1.4 Press 'Show Graphics' to generate a time series plot of price and barplot of volume
1.4.1 You can use the cursor to locate which price or volume you want to check
1.4.2 Click on the line or bar will print the date and statistics
1.4.3 You can choose the background of the plot by choosing one of the radio button
2. Statistical Measures
2.1 First enter the column you want to see these measures(CASE SENSITIVE: Open, High, Low, Close, Adj Close)
2.2 Enter the period you want to see for the measures(applicable to sma, std, boll and sharpe)
2.3 Check the desired measures and press 'Show Measures'. This will print the selected measures
2.4 To see the measures, you have to enter the all the information in 1, column name and period in 2.
3. Portfolio Management
3.1 First enter a list of stock ticker symbol seperated by ','
3.2 Enter a list of positions seperated by ',' (MUST BE less than 1, and sum to 1)
3.3 Press 'Show Analysis'. The program will simulate the combination of the stock based on\nyahoo's data given 10000 as the initial investment and print out the simulated result given the initial investment
3.4 To use Portfolio Management, you have to Enter the start and end date
4. Safely exit the program by pressing the 'Safely Exit' Button
5. If you want to use your own file, check the box at very top and click 'Browse Local File'.
5.1 The file has to be a '.csv' file with exactly the same format as online data.\n(i.e., Datetime as index, all columns Must match)
5.2 You can use local file for ONLY Basic Summary and Interactive Graphics\nbut NOT Statistical Measures and Portfolio Management"""

class mywindow(Frame):
    
    """ Initialize GUI Frame"""
    
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent=parent
        
        """Assign and position labels"""
        
        Label(root, text='Basic Summary and Interactive Graphics').grid(column=0, row=1, columnspan=4)
        Label(root, text='Stock Ticker Symbol').grid(column=0, row=2)
        Label(root, text='Web Source').grid(column=1, row=2)
        Label(root, text='Start Date').grid(column=2, row=2)
        Label(root, text='End Date').grid(column=3, row=2)

        Label(root, text='Statistical Measures').grid(column=0, row=5, columnspan=2)
        Label(root, text='Column Name').grid(column=0, row=6)
        Label(root, text='Period').grid(column=1, row=6)
        Label(root, text='Check Desired Measures').grid(column=0, row=8, columnspan=2)

        Label(root, text='Portfolio Management').grid(column=2, row=5, columnspan=2)
        Label(root, text='Stock Ticker List').grid(column=2, row=6, columnspan=2)
        Label(root, text='Position List').grid(column=2, row=8, columnspan=2)

        Label(root, text='Safely Exit Here').grid(column=2, row=11, columnspan=2)

        Label(root, justify=LEFT, text=instruction).grid(column=0, row=13, columnspan=4)
        
        """Assign and position entry boxes"""
        
        self.e1=Entry(root)
        self.e2=Entry(root)
        self.e3=Entry(root)
        self.e4=Entry(root)
        self.e5=Entry(root)
        self.e6=Entry(root)
        self.e7=Entry(root)
        self.e8=Entry(root)

        self.e1.grid(sticky=W+E, column=0, row=3)
        self.e2.grid(sticky=W+E, column=1, row=3, padx=5)
        self.e3.grid(sticky=W+E, column=2, row=3, padx=5)
        self.e4.grid(sticky=W+E, column=3, row=3)
        self.e5.grid(sticky=W+E, column=0, row=7)
        self.e6.grid(sticky=W+E, column=1, row=7, padx=5)
        self.e7.grid(sticky=W+E, column=2, row=7, columnspan=2)
        self.e8.grid(sticky=W+E, column=2, row=9, columnspan=2)

        """Assign checkbox values and position them"""
        
        self.var1=IntVar()
        self.var2=IntVar()
        self.var3=IntVar()
        self.var4=IntVar()
        self.var5=IntVar()
        self.var6=IntVar()
        self.var7=IntVar()

        Checkbutton(root, text='sma', variable=self.var1).grid(row=9, column=0, sticky=W)
        Checkbutton(root, text='std', variable=self.var2).grid(row=9, column=1, sticky=W)
        Checkbutton(root, text='boll(K=1)', variable=self.var3).grid(row=10, column=0, sticky=W)
        Checkbutton(root, text='macd(slow=20, fast=5)', variable=self.var4).grid(row=10, column=1, sticky=W)
        Checkbutton(root, text='daily_return', variable=self.var5).grid(row=11, column=0, sticky=W)
        Checkbutton(root, text='sharpe', variable=self.var6).grid(row=11, column=1, sticky=W)
        Checkbutton(root, text='Please Check This Box if Using Local Data', variable=self.var7).grid(row=0, column=0, sticky=W+E, columnspan=4)

        """Assign button functions and position buttons"""
        
        Button(root, text='Browse Local File', command=self.load_file).grid(row=4, column=0, sticky=W+E, pady=5)
        Button(root, text='Show Numerical Statistics', command=self.output).grid(row=4, column=1, sticky=W+E, padx=5, pady=5)
        Button(root, text='Show Summary', command=self.summary).grid(row=4, column=2, sticky=W+E, padx=5, pady=5)
        Button(root, text='Show Graphics', command=self.plot).grid(row=4, column=3, sticky=W+E, pady=5)
        Button(root, text='Show Analysis', command=self.showportfolio).grid(row=10, column=2, sticky=W+E, columnspan=2)
        Button(root, text='Safely Exit', command=self.close_program).grid(row=12, column=2, sticky=W+E, columnspan=2)
        Button(root, text='Show Measures', command=self.showmeasures).grid(row=12, column=0, sticky=W+E, columnspan=2)
        
    def load_file(self):
        
        """Create a pop up to find local csv file and return its path"""
        
        
        self.fname=askopenfilename(filetypes=[('csv files', '*.csv')])

        if self.fname != None:
            self.local_data = userfile_read(self.fname, self.e3.get(), self.e4.get())
        
            
    def output(self):
        
        """Print out the numerical statistics retrieved"""
        if self.var7.get() == 1:
            print self.local_data
        else:
            print get_data(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get())
            print '%s retrieved from %s from %s to %s' % (self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get())

    def summary(self):
        
        """Print out the summary statistics across the columns"""
        
        if self.var7.get() == 0:
            data=get_data(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get())
        elif self.var7.get() == 1:
            data = userfile_read(self.fname, self.e3.get(), self.e4.get())
        print data.describe()
        
    def cursor(self):
        
        """Initialize the cursors on matplotlib graphs"""
        
        self.cursor1 = Cursor(self.plot1, useblit=True, color='red', linewidth=1)
        self.cursor2 = Cursor(self.plot2, useblit=True, color='red', linewidth=1)

    def radio(self):
        
        """Initialize the radio buttons on matplotlib graphs"""
        
        rax = plt.axes([0, 0.4, 0.0852, 0.15])
        self.radio1=RadioButtons(rax, ('grey', 'wheat', 'white', 'ivory', 'tan'))

    def colorfunc(self, label):
        
        """Functionality that the radio buttons will perform when being clicked"""
        
        self.fig.set_facecolor(label)
        plt.draw()

    def plot(self):
        
        """Plot the graphics for given stock and period"""
        
        if self.var7.get() == 0:
            data=get_data(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get())
        else:
            data = userfile_read(self.fname, self.e3.get(), self.e4.get())
        self.fig, self.plot1, self.plot2=plot_stock(data)
        self.cursor()  # reference for cursor in order to show it on the graph
        self.fig.canvas.mpl_connect('pick_event', self.onpick)  # enable the graphics to be pickable
        self.radio()  # reference for the radio buttons in order to show it on the graph
        self.radio1.on_clicked(self.colorfunc)  # assign radio buttons function when it is clicked
        plt.show()

    def close_program(self):
        
        """Quit and Destroy the GUI"""
        
        root.destroy()

    def onpick(self, event):
        
        """ 
        Enable matplotlib graphics to be pickable. Upon click on the lines,
        Price and date will be printed. Upon click on bars, volume will be printed
        """
        
        if isinstance(event.artist, Line2D):
            thisline = event.artist
            xdata = thisline.get_xdata()  # get x-axis data
            ydata = thisline.get_ydata()  # get y-axis data
            ind = event.ind  # get indices of the data
            print 'Date: %s\nPrice: %s' %(np.take(xdata, ind)[0], np.take(ydata, ind)[0])  # map the x, y data with indices and print them
        elif isinstance(event.artist, Rectangle):
            patch = event.artist
            print 'Volume: %s' % patch.get_height()  # print the bar height

    def showmeasures(self):
        
        """
        Function links to the 'Show Measures' button that will print out the selected measures
        """
        
        new=stock(self.e1.get())  # initialize the inputted stock as class
        data=get_data(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get())
        column=data[self.e5.get()]  # specifying the column that will be calculated 
        if self.var1.get()==1:  # check if 'sma' is checked 
            print new.sma(column, int(self.e6.get()))  # compute sma given the column name and inputted period
            print 'Simple Moving Average for %s in %s days' %(self.e5.get(), int(self.e6.get()))
        if self.var2.get()==1:  # check if 'std' is checked
            print new.std(column, int(self.e6.get()))  # compute std given the column name and inputted period
            print 'Standard Deviation for %s in %s days' %(self.e5.get(), int(self.e6.get()))
        if self.var3.get()==1:  # check if 'boll' is checked
            print new.boll(column, int(self.e6.get()))  # compute boll given the column name and inputted period
            print 'Bollinger Bands for %s in %s days using 1 standard deviation' %(self.e5.get(), int(self.e6.get()))
        if self.var4.get()==1:  # check if 'macd' is checked
            print new.macd(column)  # compute macd given the column name and inputted period
            print 'MACD indicator for 20 slow period and 5 fast period for %s' % self.e5.get()
        if self.var5.get()==1:  # check if 'daily_return' is checked
            print new.daily_return(column)  # compute daily_return given the column name and inputted period
            print 'Daily return for %s' % self.e5.get()
        if self.var6.get()==1:  # check if 'sharpe' is checked
            print new.sharpe(column, int(self.e6.get()))  # compute the sharpe ration given the column name and period
            print 'Sharpe Ratio for %s in %s days' %(self.e5.get(), int(self.e6.get()))
        if self.var1.get()==self.var2.get()==self.var3.get()==self.var4.get()==self.var5.get()==self.var6.get()==0:  # if nothing is checked
            print 'You Have Not Chosen Any Measures Yet'
    
    def showportfolio(self):
        
        """
        Function link to 'Show Analysis' button that will simulate a combination of stock
        given the start and end date and the position percentage for each stock
        """
        
        stocklist=self.e7.get().split(',')  # separate inputted ticker string into a string list
        positionlist=self.e8.get().split(',')  # separate inputted position string into a position list
        positionlist=[float(x) for x in positionlist]  # change the position string to float numbers
        portfo=portfolio(stocklist)  # initialize the portfolio class with the inputted ticker string list
        print 'The expected result of investing 10000 for this portfolio given the position is %s' % portfo.simulate(positionlist, self.e3.get(), self.e4.get())  # simulate the portfolio
        
root = Tk()
root.title('Financial Statistics Software')
root.resizable(0,0)
mywindow(root)

if __name__=='__main__':
    root.mainloop()

