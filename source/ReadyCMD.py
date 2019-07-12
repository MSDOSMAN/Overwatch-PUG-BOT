from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from PIL import Image
import time
import pyautogui
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:/PythonTestProjects/Blink/Tesseract-OCR/tesseract'

time.sleep(8)
mouse = MouseController()
keyboard = KeyboardController()


def ReadyExecute():
    matchReadyMessage1 = "ALL PLAYERS READY ~~~ MATCH WILL BE LIVE SOON"
    time.sleep(3)
    for char in matchReadyMessage1:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.08)

    # self.Press_Choose_Preset()
    # self.Press_PUG()
    # somehow break out of the cmd loop and restart it (because it needs to look for pause)


def ReadyTracker(name):
    # searches Players for the position and changes the False to True in ReadyPlayers
    # Get this to work and get PyCharm to work with main source code
    player_pos = Players.index(name)
    ReadyPlayers[player_pos] = [name, True]

    readyCheck = True
    for q in range(0, len(ReadyPlayers)):
        if ReadyPlayers[q][1] == False:
            readyCheck = False
            break
            # could break, but this might be good for readystatus - probably no

    if readyCheck == True:
        ReadyExecute()

#Players = ['s','Kara','Stark','Nigel','Mistery','Abu','TT','Laos','Bonk','Thumb','BOIS','Rockeet'] # THIS IS FOR DEMO ONLY, WE HAVE A FUNCTION WHICH OUTPUTS THIS
Players = ['s']
#ReadyPlayers = [['s', False], ['Kara', False], ['Stark', False], ['Mistery', False], ['Abu', False], ['TT', False], ['Laos', False], ['Bonk', False], ['Thumb', False], ['BOIS', False], ['Rockeet', False], ['Nigel', False]]
ReadyPlayers = [['s', False]]
Commands = ['ready', 'pause', 'unpause', 'unready', 'readystatus']  # ready status prints who is ready and who isnt

ReadyTracker('s')