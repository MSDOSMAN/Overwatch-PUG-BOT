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

# Sample input:
# ['[s]: w', '[s]: yeeah']
# ['another message.', '[s]: w', 'The number of messages that can be sent', 'to this channel is limited, please wait to send', 'another message.', '[s]: yeeah', '[s]: boi', '[s]: %ready%']

def CMDswitch(cmdCode):
    if cmdCode == 0:
        # call ready function[s]
        None
    elif cmdCode == 1:
        # call pause function[s]
        None
    elif cmdCode == 2:
        # call unpause function[s]
        None
    elif cmdCode == 3:
        # call unready function[s]
        None
    elif cmdCode == 4:
        # call readystatus function[s]
        None

def OCRAnalysis(text):
    ChatStringArray = text

    for c in range(0, len(ChatStringArray)):
        ChatString = ChatStringArray[c]

        nameString = ''
        nameRecording = None
        nameCounter = 0
        for x in range(0, len(ChatString)):
            testChar = ChatString[x]

            if nameRecording:  # == True
                nameString = nameString + testChar
                nameCounter = nameCounter + 1

            if testChar == '[':
                nameRecording = True

            if nameCounter > 12:
                break

            if testChar == ']':
                nameString = nameString[:-1]
                break

        validName = nameString in Players

        commandString = ''
        commandRecording = None

        if validName:
            for y in range(x, len(ChatString)):
                testChar = ChatString[y]

                if commandRecording == True and testChar == '%':
                    break
                    # end of command

                if commandRecording:  # == True
                    commandString = commandString + testChar

                if testChar == '%':
                    commandRecording = True

            if commandString in Commands:
               # make it understand which command it is, then link to those functions
               cmdPosition = Commands.index(commandString)
               CMDswitch(cmdPosition)
            else:
                None
        else:
            None

Commands = ['ready', 'pause', 'unpause', 'unready', 'readystatus']  # ready status prints who is ready and who isnt
Players = ['s']

testInput = ['ina $£2 a ', '[s]: w', '[s]: yeeah', '[s]: %ready%']
OCRAnalysis(testInput)