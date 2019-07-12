import pyautogui
from PIL import Image
import pytesseract
import os
from fuzzywuzzy import fuzz
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
import time

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

'''image = Image.open('MonoTest.png')
image = image.convert('1')
image.save('MonoTest3.png')'''

'''Plan is to convert every pixel that isnt yellow into black, then crop and check if OCR works better'''

image = Image.open('MonoTest.png')

pixels = image.load()

for x in range(image.size[0]):
    for y in range(image.size[1]):
        r, g, b, a = pixels[x, y]

        if (r <= 255 and r > 240 and g <= 225 and g >= 215 and b <= 88 and b >= 78):
        #(r <= 255 and r > 240 and g <= 225 and g >= 215 and b <= 88 and b >= 78) or (r <= 227 and r > 217 and g <= 97 and g >= 87 and b <= 42 and b >= 32) or (r <= 255 and r > 245 and g <= 185 and g >= 175 and b <= 67 and b >= 57) or (r <= 236 and r > 226 and g <= 132 and g >= 122 and b <= 61 and b >= 51) or (r <= 255 and r > 245 and g <= 181 and g >= 171 and b <= 68 and b >= 58):  # interesting why all and, check the other areas where cropping is used??
        #if r <= 255 and r >= 217 and g <= 225 and g >= 150 and b <= 88 and b >= 32:
            pixels[x, y] = (0, 0, 0)
        else:
            pixels[x, y] = (255, 255, 255)

            # In the actual code, this will have to be multicored for speed - this will be a multicore within a multicore
            # So check whether that works

image.save('BlackOutTest.png')

image.crop((231, 554, 2358, 858)).save('BlackOutCrop.png')

image2 = Image.open('BlackOutCrop.png')

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