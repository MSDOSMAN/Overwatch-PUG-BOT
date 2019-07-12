from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from PIL import Image
import time
import pyautogui
import os
import pytesseract
from fuzzywuzzy import fuzz


pytesseract.pytesseract.tesseract_cmd = 'D:/PythonTestProjects/Blink/Tesseract-OCR/tesseract'

time.sleep(8)
mouse = MouseController()
keyboard = KeyboardController()

# Clearly, OCR does not work as accurately as needed in this case. To combat this, we need to change the team names
# so that they are consistent and easy for OCR. For instance RED WINS! and BLUE WINS! Instead of the "TEAM" + cap name +
# "WINS!". We need to retroactively fit this in - change team sort and change this code good luck!

def WinnerScreenShot():
    image = pyautogui.screenshot('WinnerScreen.png', region=(751, 1314, 146, 46))
    image2 = Image.open('WinnerScreen.png')
    text = pytesseract.image_to_string(image2, lang='eng')
    print(text)
    return text

def WinnerScreenShotDelete():
    os.remove('WinnerScreen.png')

def WinnerProcessing(text):
    match_ratios_team1 = []
    match_ratios_team2 = []

    for x in Team1:
        match_ratios_team1.append(fuzz.ratio(text, x))
    for y in Team2:
        match_ratios_team2.append(fuzz.ratio(text, y))

    if max(match_ratios_team1) > 50 or max(match_ratios_team2) > 50:
        if max(match_ratios_team1) > max(match_ratios_team2):
            # player from team 1 detected, so team 2 won
            print("team 2 wins!")
            return True
        else:
            print("team 1 wins!")
            return True
    else:
        return False

cap1 = 'c'
cap2 = 'h'

Team1 = ['EASY ANA', 'EASY BASTION', 'EASY LÚCIO', 'EASY MCCREE', 'EASY ROADHOG', 'EASY REAPER']
Team2 = ['EASY MEI', 'EASY SOLDIER:76', 'EASY SOMBRA', 'EASY TORBJÖRN', 'EASY ZARYA', 'EASY ZENYATTA']

winner_found = False

while winner_found == False:
    winner_found = WinnerProcessing(WinnerScreenShot())
    if winner_found == False:
        WinnerScreenShotDelete()
