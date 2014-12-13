
# Programming for Data Science: Final Project

## Team Members

Peter Li (PHL232)

Israel Malkin (IM965)

## What is it

For our project, we wrote a Python package (**portfolioFactory**) that streamlines the process for building cross-sectional trading strategies/factors. In our examples, we show how you can easily use **portfolioFactory** to implement [**momentum**][momentum] strategies (i.e. buy the winners) with different horizons and selection criteria. In addition, we include an example to show how this approach can be extened to build generic cross-sectional strategies.
 
As discussed, we created 3 examples that make use of our package. Examples can be run from the main directory. For example: 

```
python example1.py
```

The data for the examples can be found in /ExampleData. The examples will return a series of plots showing the risk/return characteristics of the specified strategy. Additionally, the example will return a portoflio object. 

[momentum]: http://faculty.chicagobooth.edu/tobias.moskowitz/research/JF_12021_TMcomments.pdf

## Dependencies

Our project was tested to work using Python 2.7 on both Windows 8 and Ubuntu 15.04 systems. In addition to **portfolioFactory** the following packages are required for basic functionality:

- [NumPy](http://www.numpy.org): 1.7.0 or higher
- [SciPy](http://www.scipy.org): miscellaneous statistical functions
- [matplotlib](http://matplotlib.sourceforge.net/): for plotting
- [Pandas](http://pandas.pydata.org/): 0.15.1
- [TkInter](http://tkinter.unpythonic.net/wiki/How_to_install_Tkinter): Used for GUI. This package should be built in. 
- [Seaborn](http://stanford.edu/~mwaskom/software/seaborn/): Plotting

	```
	pip install seaborn
	```
Please see **portfoliFactory** documentation for additional details. 

## License
MIT

## Documentation

See example ipython notebooks in /Examples

