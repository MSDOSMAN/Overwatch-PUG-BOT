from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from PIL import Image
import time
import pyautogui
import os
import pytesseract
from fuzzywuzzy import fuzz

# Big potential for multicore processing in both this and the part of the script which reads both text cmds - processes it etc

# This is being put on hold as well - too time consuming considering all of the possibilities that need to be accounted for
def Feed_Screenshot():
    image = pyautogui.screenshot('FeedScreenshot.png', region=())