import PySimpleGUI as sg                  #Used for all UI elements.
import json                               #Used for storage.
from datetime import datetime             #Used for sorting diaries.
from modules import *

#Fonts
DISPLAY_FONT = 'Helvetica 15' #Diary font.
LINE_FONT = 'Helvetica 12'

#Global variables
lst_diary = []

#Initial Setup
data = get_json()
run_count = data["run_count"]                #Assigns run count to global varible.
app_name = data["app_name"]
dict = data["diary_dict"]
if run_count == 0:                           #If the program has been run 0 times,
    do_noting = 0
else:
    not_setup()

#Change theme
sg.theme('DarkAmber')

#Creates menu bar
menu_def = [['File', ['Save']],
['Settings', ['Reset Aspects', 'Reset All Settings', 'License']],
['About', ['Licence', 'Contact']]
]

#Create First Column
rating_tutorial = "\nYou can also add a rating for each aspect of your life."

linebyline = 'Type your diary line by line and submit once done.\nSelect old diaries from list.' + rating_tutorial

left_col = [[sg.Text("Welcome to %s!" % (app_name), font = LINE_FONT),
            sg.Text("", key = '-DONE-', size = (100,1))],[sg.Input(key =
            "-IN-", size = (150, 2)), sg.Submit(key = "-SUB-")],[sg.Button("Clear Input", key =
            "-CLR-"),sg.Button("Submit Diary", key = "-SUB2-"),
            sg.Button("Delete Diary", key = "-DEL-"), sg.Text("", size =
            (100,1)), sg.Button("Show Graphs", key =
            "-GRA-")],[sg.Multiline(size = (105, 30), key =
            "-FULL-", default_text = linebyline, font = DISPLAY_FONT)]]

#Create Second Column
right_col = [[sg.Listbox(list(dict.keys()), enable_events = True, size = (30, 50),
             auto_size_text=True, key='-DISPLAY-')]]

#Assembles Layout
layout = [[sg.Menu(menu_def)],[sg.Column(left_col), sg.VSeperator(), sg.Column(right_col)]]

#Grab run_count.
run_count = get_run_count()

#Submits diary.
def sub_2():
    if get_run_count() == 0:
        set_aspects()
    global lst_diary
    lst_diary.append(rate_aspects())
    data = get_json()
    diary_dict = data["diary_dict"]                           #Assigns diary_list to local variable.
    with open('appinfo.json', 'w+') as json_file:             #Opens file w/ write, clearing file.
        now = datetime.now()                                  #Fetches current time.
        diary_dict[title()] = '\n'.join(map(str, lst_diary))  #Adds new entry with timestamp to internal dict.
        data["diary_dict"] = diary_dict                       #Changes one value in internal list.
        json.dump(data, json_file)                            #Dumps old and new data to json.
    window['-FULL-'].update('')
    window['-DONE-'].update('Entry Submitted!')
    lst_diary = []                                            #Clears current diary.
    window['-DISPLAY-'].update(list(diary_dict.keys()))       #Updates list of diaries.

#Creates window
window = sg.Window("Home", layout)                                    #Creates window with layout.
if run_count > -1:
    while True:                                                       #Runs loop until closed by user.
        events, values = window.read()                                #Reads the window/layout data.
        if events == sg.WIN_CLOSED:                                   #Awaits window close event.
            break
        if events == '-SUB-':                                         #If submit key is pressed.
            data = values["-IN-"]                                     #Fetches input.
            lst_diary.append(data)                                    #Appends input to global list.
            window['-FULL-'].update('\n'.join(map(str, lst_diary)))   #Pushes all elements of list to display.
            window['-IN-'].update('')                                 #Clears input window.
        if events == '-SUB2-' or events == 'Save':                    #Awaits submit diary key.
            sub_2()
        if events == '-CLR-':                                         #Awaits clear or submit key.
            window['-IN-'].update('')                                 #Updates input field with blank text.
        if events == '-DISPLAY-':
            try:
                with open("appinfo.json", "r") as json_file:          #Opens json file w/ read.
                    data = json.load(json_file)                       #Creates internal dictionary with json data.
                    diary_dict = data["diary_dict"]                   #Extracts diary dict from intermal list.
                ind = window[events].get()                            #Gets index for selected listbox element.
                window['-FULL-'].update(diary_dict[str(ind[0])])      #Updates display with matching diary entry with index.
            except:
                continue
        if events == '-DEL-':
            data = get_json()
            diary_dict = data["diary_dict"]
            with open('appinfo.json', 'w+') as json_file:             #Opens file w/ write, clearing file.
                diary_dict.pop(str(ind[0]), None)                     #Removes listbox index from list.
                data["diary_dict"] = diary_dict                       #Changes one value in internal list.
                json.dump(data, json_file)                            #Updates json_file.
            window['-FULL-'].update('')                               #Updates diary viewer with nothing.
            window['-DISPLAY-'].update(list(diary_dict.keys()))       #Updates list of diaries.
            window['-DONE-'].update('Entry Deleted!')                 #Displays user feedback.
        if events == 'Reset Aspects':
            set_aspects()
        if events == 'Reset All Settings':
            if set_settings() == True:
                window['-DISPLAY-'].update('')                            #Updates list of diaries.
                set_aspects()
        if events == 'Licence':
            license()
        if events == '-GRA-':
            show_total_graph()
