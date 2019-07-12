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

class gameStartup:
    def __init__(self):
        a = -1

    def Press_ShowLobby(self):
        keyboard.press(Key.esc)
        time.sleep(0.02)
        keyboard.release(Key.esc)
        time.sleep(0.02)
        keyboard.press(Key.esc)
        time.sleep(0.02)
        keyboard.release(Key.esc)
        time.sleep(0.02)
        # exits chat and opens esc menu

        mouse.position = (1280, 720)
        time.sleep(0.02)
        mouse.click(Button.left, 1)

    def Press_Settings(self):
        mouse.position = (2000, 400)
        time.sleep(2)
        mouse.click(Button.left, 1)
        time.sleep(1)

    def Press_Preset(self):
        mouse.position = (300, 350)
        time.sleep(2)
        mouse.click(Button.left, 1)

    def Press_PUG(self):
        mouse.position = (400, 600)
        time.sleep(2)
        mouse.click(Button.left, 1)
        time.sleep(0.04)

    def Press_ApplyPreset(self):
        mouse.position = (1280, 860)
        time.sleep(2)
        mouse.click(Button.left, 1)
        time.sleep(0.5)
        keyboard.press(Key.esc)
        time.sleep(0.5)
        keyboard.release(Key.esc)
        time.sleep(0.5)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)

    def Press_BackToLobby(self):
        mouse.position = (1000, 1200)
        time.sleep(0.2)
        mouse.click(Button.left, 1)
        time.sleep(0.2)

    def Press_StartGame(self):
        mouse.position = (1280, 1250)
        time.sleep(1)
        mouse.click(Button.left, 1)
        time.sleep(1)
        time.sleep(8)
        keyboard.press(Key.enter)
        time.sleep(0.2)
        keyboard.release(Key.enter)
        time.sleep(0.2)

testObj = gameStartup()

time.sleep(3)
testObj.Press_ShowLobby()
testObj.Press_Settings()
testObj.Press_Preset()
testObj.Press_PUG()
testObj.Press_ApplyPreset()
testObj.Press_BackToLobby()
# THIS IS NOT USED IN THIS ORDER
# THERE WILL BE A SORTING MODULE WHICH WOULD BE RAN HERE
# THIS IS FOR TESTING ONLY!!!
testObj.Press_StartGame()
# SOMETHING TO SEND IT BACK INTO THE IMAGE PROCESSING LOOP
# ALSO START RECORDING AND DISABLE %ready% AS IT WOULD MESS EVERYTHING UP!!!