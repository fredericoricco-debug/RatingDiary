<h1>Welcome to RatingDiary!</h1>

<h2>Setup</h2>
This application is a diary app that uses PySimpleGUI. The first part of the readme is useful for setting up, and the rest is just more details.

To run or compile into an app, first install (with pip):

> pip install PySimpleGUI numpy matplotlib

Then, run:

>> python main.py
>or
>> python3 main.py

You can edit the source code of the .json files (most importantly app_name and max_rating in appinfo.json) to your liking to modify the settings before making the python program into a macOS application.

You can install it for macOS yourself using the setup.py or use the file in ../dist/
The python command that does this is *[py2app](https://pypi.org/project/py2app/)*. You can read about *[py2exe](https://pypi.org/project/py2exe/)* to create an .exe for windows.

You can create a distribution version with py2app. The current version at the time of writing this (03/2021) doesn't work perfectly each time, but is an active project. To install this app, just place the py2app folder in your project folder and run:

> python3 setup.py py2app

Good Luck!

<h2>About</h2>

This program was made for fun by Frederico Richardson. It was also made to learn about how to program a GUI using PySimpleGUI.

<h2>Program Features</h2>

RatingDiary! has the following features:

- a linebyline input
- a multiline editable display
- diary save and delete
- life aspect rating
- display life aspect rating

<h2>Goals</h2>

At the moment, this program does very little, but it's a nice foundation to something that I would personally use for diary keeping. The goal is to make it more than just a foundation. Here are the goals ordered from most important to least important (imo).

- better data storage:

Not sure what yet but it needs to be organised and probably more efficient. I will not be doing one yet though, as it isn't as fun and can be done anytime. The longer I delay it, the worse it gets though...

- visual representation of data:

Very simple and done with matplotlib, most likely. Could be bar charts. Could be something more complicated. Will make updating data storage more complicated in future. Trying to figure out how to display "dynamic" data... If the user only has two diaries, it becomes complicated to scale the graph and so on. A solution to this would be to only show visual representations once a certain number of diaries have been created.

- lifecounter:

Currently, the program only supports the input of the diary itself and exactly three aspects to rate. Another user input could be things they want to measure, such as how many minutes they exercised or how many times they ate. These could then be tallied up and displayed as graphs as well.

- more settings:

I'd like to add some settings within the app that allow the user to change the max_rating, the app_name, and possibly the number of aspects. 

- better look:

Might be challenging and require to change GUI tool. This is why this feature is so low on the list. Otherwise it would be first xD! Making this look nice will either require PySimpleGUI to add some features to the tool, or using another library. This would probably force me to rebuild 99% of RatingDiary! I will do this when it has more features, so that the modular approach I'm taking pays off; and making a new GUI with the functions will be a piece of cake.

- about page
