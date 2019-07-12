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


class General:
    def __init__(self):
        a = -1

    def Mouse_Center(self):
        mouse.position = (1280, 720)
        time.sleep(0.1)


class PreGameSetup:
    def __init__(self):
        a = -1

    def Press_Play(self):
        mouse.position = (120, 320)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)

    def Press_CustomGame(self):
        time.sleep(0.5)
        mouse.position = (2000, 720)
        time.sleep(0.5)
        mouse.click(Button.left, 1)
        time.sleep(0.1)

    def Press_Create(self):
        mouse.position = (2400, 300)
        time.sleep(0.5)
        mouse.click(Button.left, 1)
        time.sleep(0.5)

    def Press_Settings(self):
        mouse.position = (2000, 400)
        time.sleep(2)
        mouse.click(Button.left, 1)
        time.sleep(0.1)

    def Press_Preset(self):
        mouse.position = (300, 350)
        time.sleep(2)
        mouse.click(Button.left, 1)

    def Press_Warmup(self):
        mouse.position = (400, 400)
        time.sleep(2)
        mouse.click(Button.left, 1)

    def Press_ApplyPreset(self):
        mouse.position = (1280, 860)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        keyboard.press(Key.esc)
        time.sleep(0.1)
        keyboard.release(Key.esc)
        time.sleep(0.1)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)

    def Press_StartPreGame(self):
        mouse.position = (1280, 1250)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        time.sleep(12)
        keyboard.press(Key.enter)
        time.sleep(0.2)
        keyboard.release(Key.enter)
        time.sleep(0.2)

    def Move_ToSpectator(self):
        mouse.position = (1920, 400)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        mouse.position = (320, 600)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        mouse.position = (2240, 620)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        mouse.position = (1920, 400)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)


class PlayerInvite:

    def __init__(self, Players):
        self.PlayerList = Players

    def Press_Invite(self):
        mouse.position = (2150, 400)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)

    def Press_BattleTag(self):
        mouse.position = (1550, 410)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)

    def Type_PlayerName(self, Number):
        for char in self.PlayerList[Number]:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.1)
        time.sleep(0.1)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        time.sleep(0.1)


GenObj = General()
SetupObj = PreGameSetup()

playerlist = ['s#25234', 'Kara#125323355', 'Stark#215135', 'Nigel#254252', 'Mistery#232356452', 'Abu#231412452',
              'TT#23456432', 'Laos#23454362', 'Bonk#2313452', 'Thumb#23341452', 'BOIS#23325452', 'Rockeet#2325233452']

#Players = ['s','Kara','Stark','Nigel','Mistery','Abu','TT','Laos','Bonk','Thumb','BOIS','Rockeet'] # THIS IS FOR DEMO ONLY, WE HAVE A FUNCTION WHICH OUTPUTS THIS
Players = ['s']
#ReadyPlayers = [['s', False], ['Kara', False], ['Stark', False], ['Mistery', False], ['Abu', False], ['TT', False], ['Laos', False], ['Bonk', False], ['Thumb', False], ['BOIS', False], ['Rockeet', False], ['Nigel', False]]
ReadyPlayers = [['s', False]]
Commands = ['ready', 'pause', 'unpause', 'unready', 'readystatus']  # ready status prints who is ready and who isnt

Team1 = ['s#25234', 'Kara#125323355', 'Stark#215135', 'Nigel#254252', 'Mistery#232356452', 'Abu#231412452']
Team2 = ['TT#23456432', 'Laos#23454362', 'Bonk#2313452', 'Thumb#23341452', 'BOIS#23325452', 'Rockeet#2325233452']
Cap1 = 's'
Cap2 = 'TT'

InviteObj = PlayerInvite(playerlist)

GenObj.Mouse_Center()
SetupObj.Press_Play()
GenObj.Mouse_Center()
SetupObj.Press_CustomGame()
GenObj.Mouse_Center()
SetupObj.Press_Create()
GenObj.Mouse_Center()

SetupObj.Press_Settings()
GenObj.Mouse_Center()
SetupObj.Press_Preset()
GenObj.Mouse_Center()
SetupObj.Press_Warmup()
GenObj.Mouse_Center()
SetupObj.Press_ApplyPreset()
GenObj.Mouse_Center()
SetupObj.Move_ToSpectator()
GenObj.Mouse_Center()

for x in range(0, 11):
    InviteObj.Press_Invite()
    GenObj.Mouse_Center()
    InviteObj.Press_BattleTag()
    InviteObj.Type_PlayerName(x)

GenObj.Mouse_Center()
SetupObj.Press_StartPreGame()