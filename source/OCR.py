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


def ReadyOCR(screenshotNum):
    image = Image.open('BlinkCommandSC' + str(screenshotNum) + '.png')
    text = pytesseract.image_to_string(image, lang='eng')
    '''keyboard.press(Key.alt)
    keyboard.press(Key.tab)
    keyboard.release(Key.alt)
    keyboard.release(Key.tab)'''
    #self.testText = text
    # REMOVE ME
    #print(self.testText)
    return text


def OCRtoAnalysis(text):
    output = []
    tempString = ''
    for char in text:
        tempString = tempString + char
        if char == '\n':
            output.append(
                tempString[:-1])  # [:-1] will remove the \n at the end of the statement. This could be useful however
            tempString = ''

    newlinecheck = '\n' not in output  # True - good, False - bad
    emptylinecheck = '' not in output
    blanklinecheck = ' ' not in output

    while newlinecheck == False:
        output.remove('\n')
        newlinecheck = '\n' not in output
    while emptylinecheck == False:
        output.remove('')
        emptylinecheck = '' not in output
    while blanklinecheck == False:
        output.remove(' ')
        blanklinecheck = ' ' not in output
    text = output

    print(text)

time.sleep(3)
for x in range(0, 5):
    OCRtoAnalysis(ReadyOCR(x))
