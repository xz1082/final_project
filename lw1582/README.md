
NYC Free Wifi Project 
======================
Created by Lucy Wang and Maya Rotmensch.
Last Edits made: 12/13/2014


CONTENTS OF THIS FILE
----------------------
 * Introduction
 * Requirements
 * How to run 
 * Expected results


INTRODUCTION
------------

This program was created to help users identify public Wi-Fi locations that are closest to an address-of-interest.
To do so, the user provides an address in NYC, including all 5 boroughs. The program analyzes the address and presents the 5 nearest Wifi hot-spots to the user in table and map format. The table output includes the following information about the WiFi spot: Name, Location, Location Type, SSID, WiFi Type, and Distance. To help the user locate these hot-spots easily, a map is provided with markers to indicate both the address the user searched for (in blue), and the locations of the hot-spots (red) numbered in the same order as the table. To help the user better understand the distribution of WiFi spots in the city, the program also produces and saves several figures displaying statistics about the free Wifi locations in NYC.


REQUIREMENTS
-------------
In order to run this program successfully, you must ensure the following packages installed:
(It is possible that the program will run without problem on earlier versions of the required packages. However to ensure optimal performance, please )

    * This program runs on Python 2.7.
    * matplotlib - version 1.4.0
        can be installed via pip install matplotlib
    * pandas - version 15.1
        can be install via pip install pandas
    * numpy - version 1.9.0
        can be downloaded from http://sourceforge.net/projects/numpy/files/
    * pygeocoder
        can be installed via pip install pygeocoder
    * motionless
    	source for motionless can be found here: https://github.com/ryancox/motionless
        can be installed via pip install motionless


HOW TO RUN
-----------
To run the program, please navigate to the Project folder where you will find main.py. The entire program is initiated when running : **python main.py** from your terminal. 


EXPECTED RESULTS
----------------

When the program is run from the project folder via **python main.py** a prompt should appear in the terminal, prompting the user to input an address located in NYC. 
Examples of valid input are:

    * 726 Broadway 
    * 726 broadway new york

If the user input cannot be automatically decoded by the pygeocoder module, the program will attempt to auto correct the address. If the address cannot be corrected, the user will be prompted to enter the address again.

Once the user inputs a valid address:

    * A list of the 5 closest Wifi locations will be showed on the terminal screen with useful characteristics to help the user locate the hot-spot (such as: Name of hot-spot, location, location type, SSID - the name of network the user should look for, the type of the network - either free or limited-free, and the distance from the entered address). 
    * A map of the relevant area in NYC will be displayed with a blue marker labeling the address the user searched for (in blue), and markers denoting the locations of the hot-spots (red).
    * a heat-map figure showing the concentration of Wifi networks by a given provider will be saved to file as "heatmap.pdf"
    * a bar chart showing the number of free Wifi networks by borough, saved as 'Free Wifi by Borough.png'

after the output it displayed, the user will be prompted to either:

    * type 'Y' to displayed the next 5 results ordered by distance from origin
    * type 'C' to search to a different address
    * type any other key to quit the program.



''' Readme Template from https://www.drupal.org/node/2181737'''