from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from PIL import Image
import time
import pyautogui
import os
import pytesseract
from fuzzywuzzy import fuzz

'''     
MAJOR ISSUE:
I CANT GET MOUSE CONTROLS TO WORK INSIDE OF OVERWATCH. IT SIMPLY IGNORES THE MOVEMENT CREATED BY AUTOGUI AND PYNPUT
LEAVE THIS OUT FOR NOW AND INSTEAD JUST ANALYZE THE FEED
'''

'''
Potential fix: left get to a certain height and just press left click: players will be tracked
I think this is still very time consuming and challenging - it is necessary however - implement later 
'''

pytesseract.pytesseract.tesseract_cmd = 'D:/PythonTestProjects/Blink/Tesseract-OCR/tesseract'

time.sleep(4)
mouse = MouseController()
keyboard = KeyboardController()

def Lij_Cam():
    keyboard.press('d')
    keyboard.press('s')
    time.sleep(4)
    keyboard.release('d')
    keyboard.release('s')
    time.sleep(90)
    mouse.click(Button.left, 1)
    time.sleep(3)
    mouse.click(Button.left, 1)
    time.sleep(1)
    mouse.click(Button.left, 1)
    keyboard.press('e')
    time.sleep(4)
    keyboard.release('e')

    # add while loop which ends once round has finished


def Map_Switch(map_index):
    if map_index == 0:
        # Han
        a = 0
    elif map_index == 1:
        # Hor
        a = 0
    elif map_index == 2:
        # Temp
        a = 0
    elif map_index == 3:
        # Volk
        a = 0
    elif map_index == 4:
        # Blizz
        a = 0
    elif map_index == 5:
        # Eich
        a = 0
    elif map_index == 6:
        # Holly
        a = 0
    elif map_index == 7:
        # King
        a = 0
    elif map_index == 8:
        # Num
        a = 0
    elif map_index == 9:
        # Ilio
        a = 0
    elif map_index == 10:
        # Lij
        a = 0
    elif map_index == 11:
        # Nepal
        a = 0
    elif map_index == 12:
        # Oasis
        a = 0
    elif map_index == 13:
        # Dorado
        a = 0
    elif map_index == 14:
        # Junk
        a = 0
    elif map_index == 15:
        # Rialto
        a = 0
    elif map_index == 16:
        # Route
        a = 0
    elif map_index == 17:
        # Watch
        a = 0

def Find_Map():
    image = pyautogui.screenshot('Current_Map.png', region=(85, 369, 355, 29))
    image2 = Image.open('Current_Map.png')
    text = pytesseract.image_to_string(image2, lang='eng')

    match_ratios = []

    for map in map_list:
        match_ratios.append(fuzz.ratio(text, map))

    highest_ratio_index = match_ratios.index(max(match_ratios))




    # add fuzzywuzzy and determine which map is being played
    # then, depending on the map, run a specific function which controls the camera position REMEMBER TO ADD SOMETHING ALLOWING IT TO KNOW WHEN A NEW ROUND IS BEING PLAYED/ POINT HAS BEEN CAPPED/ FOLLOW THE CART
    # then a function that starts recording

map_list = ['HANAMURA', 'HORIZON LUNAR COLONY', 'TEMPLE OF ANUBIS', 'VOLSKAYA INDUSTRIES', 'BLIZZARD WORLD', 'EICHENWALDE', 'HOLLYWOOD', 'KING\'S ROW', 'NUMBANI', 'ILIOS', 'LIJIANG TOWER', 'NEPAL', 'OASIS', 'DORADO', 'JUNKERTOWN', 'RIALTO', 'ROUTE 66', 'WATCHPOINT: GIBRALTAR']
# Find_Map()

Lij_Cam()
