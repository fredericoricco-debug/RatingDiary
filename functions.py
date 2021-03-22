import json
import PySimpleGUI as sg
from datetime import datetime             #Used for sorting diaries.
import numpy as np
import matplotlib.pyplot as plt

#Returns json_file data as dict.
def get_json():
    with open("/Users/admin/Documents/Projects/RatingDiary/appinfo.json", "r") as json_file: #Opens json file w/ read.
        data = json.load(json_file)              #Creates internal list with json data.
        return data

#Updates run count in json_file.
def update_run_count(run_count):
    data = get_json()
    with open("/Users/admin/Documents/Projects/RatingDiary/appinfo.json", 'w+') as json_file:         #Opens file w/ write, clearing file.
        data["run_count"] = run_count                     #Changes one values in internal list.
        json.dump(data, json_file)                        #Dumps entire list into cleared json file.

def get_run_count():
    data = get_json()
    return data["run_count"]

#Updates an aspect in json_file.
def update_aspect(key, aspect):
    data = get_json()
    with open("/Users/admin/Documents/Projects/RatingDiary/appinfo.json", 'w+') as json_file:         #Opens file w/ write, clearing file.
        data[key] = aspect                                #Changes one values in internal list.
        json.dump(data, json_file)                        #Dumps entire list into cleared json file.

#Sets each aspect according to user input.
def set_aspects():
    temp_var = False
    layout = [
    [sg.Text('This will allow you to rate your own performance.')],   #Sets layout.
    [sg.Text('Please enter three aspects of your life that need improvement.')],
    [sg.Text('Aspect 1', size=(10, 1)), sg.InputText(key = "-AS1-")],
    [sg.Text('Aspect 2', size=(10, 1)), sg.InputText(key = "-AS2-")],
    [sg.Text('Aspect 3', size=(10, 1)), sg.InputText(key = "-AS3-")],
    [sg.Submit()]
]
    window = sg.Window('Set Aspects', layout)
    event, values = window.read()
    window.close()
    #If no values are inputted it runs itself.
    if event == sg.WIN_CLOSED:
        temp_var = True
    if (
            values["-AS1-"] == "" or
            values["-AS2-"] == "" or
            values["-AS3-"] == ""
        ):
        sg.popup("Please input 3 aspects.")
        set_aspects()
    elif temp_var == False:
        update_run_count(1)
        for i in range(3):
            var = "-AS%s-" % (i+1)
            update_aspect(var, values[var])  #Takes both key and data for aspect.

def not_setup():
    update_run_count(get_run_count()+1)

def get_aspect(int):
    data = get_json()
    return data['-AS%s-' % (int)]

def get_max_rating():
    data = get_json()
    return data["max_rating"]

def process(AS1, AS2, AS3):
    with open("/Users/admin/Documents/Projects/RatingDiary/aspectsdata.json", "r") as json_file: #Opens json file w/ read.
        data = json.load(json_file)              #Creates internal list with json data.
        return data
    for i in range(1, 6):
        data[str(i)] = data[str(i-1)]
    temp = data["0"]
    temp["AS1"] = int(AS1)
    temp["AS2"] = int(AS2)
    temp["AS3"] = int(AS3)
    data["0"] = temp
    with open("/Users/admin/Documents/Projects/RatingDiary/aspectsdata.json", 'w+') as json_file:         #Opens file w/ write, clearing file.
        json.dump(data, json_file)

def rate_aspects():
    max_rating = get_max_rating()
    AS1 = get_aspect(1)
    AS2 = get_aspect(2)
    AS3 = get_aspect(3)
    layout = [
    [sg.Text('Rate each aspect for today.')],   #Sets layout.
    [sg.Text(AS1, size=(10, 1)), sg.InputText(key = "-AS1-"), sg.Text('/%s' % (max_rating), size=(4, 1))],
    [sg.Text(AS2, size=(10, 1)), sg.InputText(key = "-AS2-"), sg.Text('/%s' % (max_rating), size=(4, 1))],
    [sg.Text(AS3, size=(10, 1)), sg.InputText(key = "-AS3-"), sg.Text('/%s' % (max_rating), size=(4, 1))],
    [sg.Submit()]
]
    window = sg.Window('Rate Aspects', layout)
    event, values = window.read()
    window.close()
    #If no values are inputted it runs itself.
    if event == sg.WIN_CLOSED:
        return ""
    if (
            values["-AS1-"] == "" or
            values["-AS2-"] == "" or
            values["-AS3-"] == ""
        ):
        sg.popup("Please input 3 ratings.")
        return rate_aspects()
    else:
        aspect_1 = "\n" + AS1 + ": " + values["-AS1-"] + '/%s' % (max_rating) + "\n"
        aspect_2 = AS2 + ": " + values["-AS2-"] + '/%s' % (max_rating) + "\n"
        aspect_3 = AS3 + ": " + values["-AS3-"] + '/%s' % (max_rating)
        process(values["-AS1-"], values["-AS2-"], values["-AS3-"])
        transcript = aspect_1 + aspect_2 + aspect_3
        return transcript

def get_from_generalinfo(key):
    with open("/Users/admin/Documents/Projects/RatingDiary/generalinfo.json", "r") as json_file: #Opens json file w/ read.
        data = json.load(json_file)                  #Creates internal list with json data.
    var = data[key]
    return var

#Make a nice title.
def title():
    now = str(datetime.now())
    months = get_from_generalinfo("months")
    month = months[now[5:7]]
    year = now[0:4]
    day = now[8:10]
    time = now[11:19]
    title = day + " " + month + " " + year + ' ' + time
    return title

def reset():
    with open("/Users/admin/Documents/Projects/RatingDiary/appinfo.json", 'w+') as json_file:
        data = {}
        data["app_name"] = "RatingDiary"
        data["run_count"] = 0
        data["max_rating"] = 10
        data["diary_dict"] = {}
        data["-AS1-"] = ""
        data["-AS2-"] = ""
        data["-AS3-"] = ""
        json.dump(data, json_file)                #Dumps entire list into cleared json file.

def set_settings():
    layout = [
    [sg.Text('Reset all settings... Are you sure?')],   #Sets layout.
    [sg.Button('Yes', key = "-YES-"), sg.Button('No', key = '-NO-')]
]
    window = sg.Window('Reset Settings', layout)
    event, values = window.read()
    window.close()
    if event == sg.WIN_CLOSED or event == '-NO-':
        return False
    elif event == '-YES-':
        reset()
        return True

def license():
    license = get_from_generalinfo("license")
    layout = [
    [sg.Text('RatingDiary')],   #Sets layout.
    [sg.Text(license)]
]
    window = sg.Window('Licence', layout)
    event, values = window.read()
    window.close()
    #If no values are inputted it runs itself.
    if event == sg.WIN_CLOSED:
        return True
