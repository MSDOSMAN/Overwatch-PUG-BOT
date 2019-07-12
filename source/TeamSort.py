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

'''
So, big issue with OCR. 
We need to condense down the player slot image to be JUST the name 
Do this by scanning every pixel until RGB: 221, 154, 130 HSV: 16, 41, 87 is found then set off a flag
This flag will go down once blue (or red for team 2) is hit
The x value of the pixel once the flag goes down will be the end of the rank
The image then needs to be cropped up to that x coordinate and then can be fed through tesseract 

For team 2 this process will be different as the x coordinate cut off will be as soon as the flag is triggered. 
Then you need to crop the image from the x coordinate to the far right end of the image (contrary to team 1 where you crop from far left to x coordinate 

KEEP IN MIND THAT THIS WILL NEED TO BE EXPANDED TO THE OTHER RANK COLOURS!!!!
ALSO, WHEN TESTING WITH THE AI, THEY DON'T HAVE RANKS SO JUST CROP THOSE MANUALLY 
AND USE THOSE AS INPUT FOR THE REST OF THE PROGRAM. TEST CROPPING WITH THE s
ACCOUNT AS WELL AS SOMEONE ELSE'S ACCOUNT: c, m, ETC...

Does not work, its moving across everyone 
'''

# Maybe add captains on top


class TeamSort:
    def __init__(self, team1, team2, cap1, cap2, playerList):
        self.Players = playerList
        self.Team1 = team1
        self.Team2 = team2
        self.Captain1 = cap1
        self.Captain2 = cap2

        self.CorrectPos = []  # This contains the name of each player as well as whether they are on the correct team or not
        self.CurrentPos = []

        self.SortTuples = [(441, 634), (441, 715), (441, 795), (441, 888), (441, 967), (441, 1041), (1338, 640), (1338, 717), (1338, 798), (1338, 882), (1338, 961), (1338, 1039)]   # first 6 are team 1, last 6 are team 2

        for x in team1:  # This fills this list out
            self.CorrectPos.append([x, 1])  # This doesn't work

        for x in team2:
            self.CorrectPos.append([x, 2])


    def Take_LobbySlotSC(self):
        # This will take 12 screenshots of the players in the lobby slots
        time.sleep(3)
        for x in range(0, 6):
            image = pyautogui.screenshot('LobbySlotSC' + str(x) + '.png', region=(68, 600 + x * 82, 639, 75))
        for x in range(0, 6):
            image = pyautogui.screenshot('LobbySlotSC' + str(x + 6) + '.png', region=(1072, 600 + x * 82, 639, 75))

    def Delete_ScreenShots(self):
        for x in range(0, 12):
            os.remove('LobbySlotSC' + str(x) + '.png')

    def Image_ScannerTeam1(self, imageNum):
        image = Image.open('LobbySlotSC' + str(imageNum) + '.png')
        width, height = image.size
        rgb_image = image.convert('RGB')

        bronze_xTracker = []

        for y in range(0, height):
            for x in range(0, width):
                r, g, b = rgb_image.getpixel((x, y))

                if r > 140 and r < 220 and g > 90 and g < 160 and b > 75 and b < 140:
                    bronze_xTracker.append(x)
                    print(x)
                    print(" WAS ADDED")

        image.crop((max(bronze_xTracker), 0, width, height)).save('LobbySlotSC' + str(imageNum) + '.png') # don't know if this will work - I do want it to overwrite the existing file tho

    def Image_ScannerTeam2(self, imageNum):
        image = Image.open('LobbySlotSC' + str(imageNum) + '.png')
        width, height = image.size
        rgb_image = image.convert('RGB')

        bronze_xTracker = []

        for y in range(0, height):
            for x in range(0, width):
                r, g, b = rgb_image.getpixel((x, y))

                if r > 140 and r < 220 and g > 90 and g < 160 and b > 75 and b < 140:
                    bronze_xTracker.append(x)

        image.crop((0, 0, min(bronze_xTracker), height)).save('LobbySlotSC' + str(imageNum) + '.png')

    def Find_Position(self):
        match_ratios = []
        highest_ratios = []
        for x in range(0, 12):
            image = Image.open('LobbySlotSC' + str(x) + '.png')
            text = pytesseract.image_to_string(image, lang='eng')
            # text is now the name of the player
            # if <6, team 1, >6, team 2
            for name in self.Players:
                match_ratios.append(fuzz.ratio(text, name))

            highest_ratios.append(match_ratios.index(max(match_ratios)))

            if x < 6:
                self.CurrentPos.append([self.Players[highest_ratios[x]], 1])
                match_ratios = []
            else:
                self.CurrentPos.append([self.Players[highest_ratios[x]], 2])
                match_ratios = []


    def Swap(self, pos1, pos2):

        for x in range(0, 12):
            if pos1 == x:
                mouse.position = self.SortTuples[x]
                time.sleep(0.02)
                mouse.click(Button.left, 1)

                for y in range(0, 12):
                    if pos2 == y:
                        mouse.position = self.SortTuples[y]
                        time.sleep(0.02)
                        mouse.click(Button.left, 1)
                        break

    def Press_Move(self):  # use this to stop moving as well
        mouse.position = (2000, 400)
        time.sleep(0.5)
        mouse.click(Button.left, 1)
        time.sleep(0.5)

    def Swap_Logic(self):

        incorrectPosTeam1 = []
        incorrectPosTeam2 = []

        for x in range(0, len(self.CurrentPos)):
            for y in range(0, len(self.CorrectPos)):
                if self.CurrentPos[x][0] == self.CorrectPos[y][0]:
                    if self.CurrentPos[x][1] != self.CorrectPos[y][1]:
                        if x < 6:
                            incorrectPosTeam1.append([self.CurrentPos[x][0], x])
                        elif x > 5:
                            incorrectPosTeam2.append([self.CurrentPos[x][0], x])

        self.Press_Move()
        for z in range(0, len(incorrectPosTeam1)):
            print("Swap: " + str(incorrectPosTeam1[z][1]) + ", " + str(incorrectPosTeam2[z][1]))
            self.Swap(incorrectPosTeam1[z][1], incorrectPosTeam2[z][1])
        self.Press_Move()

    def Type_TeamName(self):
        mouse.position = (441, 580)
        time.sleep(1)
        mouse.click(Button.left, 1)

        team1_name = "team " + str(self.Captain1)
        team2_name = "team " + str(self.Captain2)

        time.sleep(0.2)

        for char in team1_name:
            time.sleep(0.02)
            keyboard.press(char)
            time.sleep(0.02)
            keyboard.release(char)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        mouse.position = (1338, 580)
        time.sleep(1)
        mouse.click(Button.left, 1)

        time.sleep(0.2)


        for char in team2_name:
            time.sleep(0.02)
            keyboard.press(char)
            time.sleep(0.02)
            keyboard.release(char)

        keyboard.press(Key.enter)
        keyboard.release(Key.enter)






'''Team1 = ['s#25234', 'Kara#125323355', 'Stark#215135', 'Nigel#254252', 'Mistery#232356452', 'Abu#231412452']
Team2 = ['TT#23456432', 'Laos#23454362', 'Bonk#2313452', 'Thumb#23341452', 'BOIS#23325452', 'Rockeet#2325233452']
Cap1 = 's'
Cap2 = 'TT'''

Players = ['EASY ANA', 'EASY BASTION', 'EASY LÚCIO', 'EASY MCCREE', 'EASY ROADHOG', 'EASY REAPER', 'EASY MEI', 'EASY SOLDIER:76', 'EASY SOMBRA', 'EASY TORBJÖRN', 'EASY ZARYA', 'EASY ZENYATTA']
Team1 = ['EASY ANA', 'EASY BASTION', 'EASY LÚCIO', 'EASY MCCREE', 'EASY ROADHOG', 'EASY REAPER']
Team2 = ['EASY MEI', 'EASY SOLDIER:76', 'EASY SOMBRA', 'EASY TORBJÖRN', 'EASY ZARYA', 'EASY ZENYATTA']
Cap1 = 'EASY ANA'
Cap2 = 'EASY MEI'

testObj = TeamSort(Team1, Team2, Cap1, Cap2, Players)

# This will cycle through and crop out the images as needed - allowing OCR to take place

testObj.Image_ScannerTeam2(2)

# Imagine that you have a set of saved images in OCR-able form now
'''
testObj.Find_Position()
testObj.Swap_Logic()
testObj.Type_TeamName()
'''