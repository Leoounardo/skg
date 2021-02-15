from random import randint
def generateKey(numbers):
    upl = randint(65,90)
    lowl = randint(97, 122)
    nb = randint(48, 57)
    key = ''
    for n in range(numbers):
        teco = randint(1, 3)
        
        if teco == 1:
            key += chr(randint(65,90))
        elif teco == 2:
            key += chr(randint(97, 122))
        else:
            key += chr(randint(48, 57))
    return key

######################################
from PySimpleGUI import PySimpleGUI as sg
from pyperclip import copy
#ly
lennumber = 8
key = generateKey(lennumber)
sg.theme('Reddit')
yn = True
ly = [
    [sg.Text(key, key= "do", visible = yn)],
    [sg.Button("copy"), sg.Button("generate key"), sg.Button("show"), sg.Button("menu")]
]
#wd
wd = sg.Window('totop', ly, size=(300,100), element_justification='c')

##
ok = 1
while ok:
    event, values = wd.read()
    if event == sg.WINDOW_CLOSED:
        ok = 0
    if event == "copy":
        copy(key)
    if event == "generate key":
        key = generateKey(lennumber)
        wd.Element("do").Update(key)
    if event == "show":
        if yn == False:
            yn = True
            wd.Element("do").Update(visible=yn)
        else:
            yn = False
            wd.Element("do").Update(visible=yn)
    if event == "menu":
        nbb = sg.popup_get_text("MAX NUMBERS", "MAXNUMBERS", lennumber)
        lennumber = int(nbb)