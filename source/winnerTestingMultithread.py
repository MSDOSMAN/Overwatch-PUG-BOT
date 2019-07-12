import pyautogui
from PIL import Image
import pytesseract
import os
from fuzzywuzzy import fuzz
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time
import threading

start_time = time.time()

pytesseract.pytesseract.tesseract_cmd = 'D:/PythonTestProjects/Blink/Tesseract-OCR/tesseract'

mouse = MouseController()
keyboard = KeyboardController()

class Bridge:
    PlayersWithTags = []
    Players = []
    Team1 = []
    Team2 = []
    Cap1 = ''
    Cap2 = ''
    text_Array = []
    ReadyPlayers = []
    AllReady = False
    LimitReady = True
    Commands = ['ready', 'pause', 'unpause', 'unready', 'readystatus', 'forfeit']
    TimeSinceRStatus = -1
    WinnerFound = False
    ForfeitPlayers = []

image = Image.open('MonoTest.png')

image.crop((231, 554, 2358, 858)).save('BlackOutCrop.png')

image = Image.open('BlackOutCrop.png')

pixels = image.load()

def FirstHalf():
    width, height = image.size

    for x in range(0, width):
        for y in range(0, int(round(height/2))):
            r, g, b, a = pixels[x, y]

            if (r <= 255 and r > 240 and g <= 225 and g >= 215 and b <= 88 and b >= 78):
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)
    #image.show()
    #input("Press anything to continue")

def SecondHalf():
    width, height = image.size

    for x in range(0, width):
        for y in range(int(round(height/2)), height):
            r, g, b, a = pixels[x, y]

            if (r <= 255 and r > 240 and g <= 225 and g >= 215 and b <= 88 and b >= 78):
                pixels[x, y] = (0, 0, 0)
            else:
                pixels[x, y] = (255, 255, 255)
    #image.show()
    #input("Press anything to continue")

'''image = Image.open('MonoTest.png')
image = image.convert('1')
image.save('MonoTest3.png')'''

'''Plan is to convert every pixel that isnt yellow into black, then crop and check if OCR works better'''

thread1 = threading.Thread(target=FirstHalf, args=())
thread2 = threading.Thread(target=SecondHalf, args=())

thread1.start()
thread2.start()
thread1.join()
thread2.join()

image.save('BlackOutTest.png')

#image.crop((231, 554, 2358, 858)).save('BlackOutCrop.png')

image2 = Image.open('BlackOutTest.png')

width, height = image2.size
m = -0.259
xshift = abs(m) * width
new_width = width + int(round(xshift))
img = image2.transform((new_width, height), Image.AFFINE,
        (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)
img.save('BlackOutSkewTest.png')

img.crop((70, 22, 2104, 274)).save('WinnerPreOCR.png')

image3 = Image.open('WinnerPreOCR.png')

image3.resize((3100, 252)).save('WinnerPreOCRStretched.png')

image4 = Image.open('WinnerPreOCRStretched.png')

text = pytesseract.image_to_string(image4, lang='eng')

print(text)

end_time = time.time()

print((end_time - start_time)*1000)