DS-GA1007 Final Project User Guide
NYC Official Job data Analysis with Visualization 
======================
## Team Member
- Qingxian Lai (ql516)
- Jianming Zhou (jz1584))
- Ke Ye (ky822)

## Table of Contents
* [What is it](#what-is-it)
* [How to run](#how-to-run)
* [Program input](#program-input)
* [Program output](#program-output)
* [Dependencies](#dependencies)
* [Demo](#an-typical-walk-through-example)


###What is it 
This program provides user the overall view of NYC Official Job Dataset in the most recent years through Data Visualization and brief job information listing. 

###How to run
For Mac User: Use the terminal, change the directory where the main function located, then type:

~~~
python main.py
~~~
For Windows User: use Command Prompt, change the directory where the main function located, then type:

~~~
py main.py
~~~

###Program input
Program takes options inputs like a, b, c etc. from the option list program provided at the beginning of the program. Program could also take a keyword input from user if user would like to search the job by keyword. 

###Program output
Program could generate different kind of plots or even a piece of Google map upon user’s request. In addition, if user searches jobs by using keyword, the program may print out a list of available jobs, or a specific job with important information in detail. 

###Dependencies

* [NumPy](http://www.numpy.org): 1.7.0 or higher
* [Pandas](http://pandas.pydata.org/): 0.15.0 or higher
* [matplotlib](http://matplotlib.sourceforge.net/): 1.3.1 or higher
* [PIL](http://www.pythonware.com/products/pil/): or you can use [Image](http://effbot.org/imagingbook/image.htm) package

All these package can be easily installed with `pip`:

~~~
$ pip install [The package name]
~~~

Or Updated with command:

~~~
$ pip install -U [The package name]
~~~


###An typical walk-through example

1.At the beginning of the program, you will see an option list:

![menu1](elements/1.png?raw=true =650x)

2.Choose one you interested in; suppose you want to know the relationship between civil level and base salaries, you could type `d`. Then the scatter-plot will pop up: 

![line plot](elements/2.png?raw=true =650x)

Close the plot window to go back

3.After that, we could also search for jobs by entering a keyword, you should first select `g` to change to a searching mode, then type your keyword, say, "manager". A list of available jobs will displayed on the screen with their job ID and business title:

![list of available jobs](elements/3.png?raw=true =650x)

At the end of this list, you will see a menu showing all the option with which you can explore the job list:

![job list menu](elements/4.png?raw=true =650x)

4.For example, you want to see all these jobs' location on a google map, you can type `m`. Then a map will pop up:

![list map](elements/5.png?raw=true =650x)

Remember to close the image window to move on

5.If you want to get more information about a specific job, select `g`, then as the prompt instrunction says, type a job id of which job you want to learn more. For example, we select the job Id `142484`. It will pop a new menu:

![one job menu](elements/7.png?raw=true =650x)

You can either select a to show the detailed infomation or select b to show its location on the map. If you want go back to the job list and explore other jobs or plot, just input `q` to go back

6.Then you may want to know the percentage of different degree requirment. Then type `a`, a pie plot will pop up:

![pie plot](elements/6.png?raw=true =650x)

7.When you decide to end this program, input `q`. Then the whole program will end.








