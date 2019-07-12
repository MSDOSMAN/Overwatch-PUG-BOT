from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from PIL import Image
import time
import pyautogui
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'D:/PythonTestProjects/Blink/Tesseract-OCR/tesseract'

class CMDscreenShots:

    def __init__(self):
        a = -1

    def ChatBoxScreenShot(self, screenshotNum):
        time.sleep(1)
        image = pyautogui.screenshot('BlinkCommandSC' + str(screenshotNum) + '.png', region=(0, 600, 640, 380)) # region changes depending on whether it is in lobby: (0, 1000, 640, 380)
        time.sleep(1)

    def ScreenShotDelete(self, screenshotNum):
        for x in range(0, screenshotNum):
            time.sleep(0.5)
            os.remove('BlinkCommandSC' + str(x) + '.png')

time.sleep(4)

scObj = CMDscreenShots()

x = 0
y = 0

for x in range(0, 5):
    scObj.ChatBoxScreenShot(x)
    y = y + 1

print("Screen shots done. Press any key to delete them")
input()

scObj.ScreenShotDelete(y)

# Screenshots seem to be bugged
# Once this is finished, keep a file with just this but then make sure to copy this other to the OCR module