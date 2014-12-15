# Financial Statistics Software
Written by Sylvia Zhao, Tian Wang and Wenxi Lei

Packed and Structured by Wenxi Lei

For complete usage details, please consult the documentation included.

### Usage of the Application

The application allows users to
* Enter a date range and stock ticker symbol and source site to access real time stock data
* Perform simple statistical analysis such as Simple Moving Average, Sharpe Ratio, etc.
* Enter a combination of stock ticker symbols and position lists to simulate given portfolio
* Import local data file to perform data analysis
* Plot stock graphics and interact with the plot(eg, pick point on the series to show price, pick bar plot to show volume)
* Customize background of the plots
* Use GUI all the time

### Version
0.0.1

### Configuration
The application is written entirely in python. Libraries used include:
* Matplotlib for graphics
* Pandas to access data and perform analysis
* Numpy to perform numerical computations
* Tkinter for Graphical User Interface


### How to Run the Program
You need Internet connection to use this application.

* Run on command line (Linux):


```sh
Change directory to the application
$ python main.py
```

* Run on command line(Windows):

```sh
Change directory to the application
$ python main.py
```

* Run on Windows without being on command line:

```sh
Double click the main.py file
```

### Known Issues

* The application runs smoothly on Windows and Linux
* **DO NOT** use Mac OS X to run this application as it may suffer cursor not showing and sudden freezing problems
* If you do not have Tkinter installed, find it on the python website as it may come along with python distribution

### Acknowledgement
Thanks Tim Wang and Sylvia Zhao for their great contribution to this application. 

Thanks Dr. Greg Watson for being a great teacher for the semester.


