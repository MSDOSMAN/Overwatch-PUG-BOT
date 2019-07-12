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


# Do this when stitching together everything
# Make it so that at least 3 people need to pause
# Then at least 3 people need to unpause
















# Players = ['s','Kara','Stark','Nigel','Mistery','Abu','TT','Laos','Bonk','Thumb','BOIS','Rockeet'] # THIS IS FOR DEMO ONLY, WE HAVE A FUNCTION WHICH OUTPUTS THIS
Players = ['s']
# ReadyPlayers = [['s', False], ['Kara', False], ['Stark', False], ['Mistery', False], ['Abu', False], ['TT', False], ['Laos', False], ['Bonk', False], ['Thumb', False], ['BOIS', False], ['Rockeet', False], ['Nigel', False]]
PausePlayers = [['s', False]]
Commands = ['ready', 'pause', 'unpause', 'unready', 'readystatus']  # ready status prints who is ready and who isnt