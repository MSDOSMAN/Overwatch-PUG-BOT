from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from PIL import Image
import time
import pyautogui
import os
import pytesseract
from fuzzywuzzy import fuzz
import threading
import multiprocessing

pytesseract.pytesseract.tesseract_cmd = 'D:/PythonTestProjects/Blink/Tesseract-OCR/tesseract'

time.sleep(8)
mouse = MouseController()
keyboard = KeyboardController()

# Used for passing variables from one module to the next
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
    Commands = ['ready', 'pause', 'unpause', 'unready', 'readystatus', 'forfeit', 'commands']
    WinnerFound = False
    ForfeitPlayers = []

    LastRS = -1 # Time of most recent readystatus
    RS_TIMER = 5 # Ready status constant timer
    CM_TIMER = 5 # Print commands timer
    PauseState = False # True = We are paused, False = We are live
    timerCheck = -1
    PauseLock = threading.Lock()
    LastRSLock = threading.Lock()
    TimeLock = threading.Lock()
    WinnerFLock = threading.Lock()

    ChatBoxSCLock = threading.Lock()
    ChatBoxSCDelLock = threading.Lock()

# Execute order
# These functions control the flow of the program
class Execute_Order:
    def __init__(self):
        pass

    def Execute_Read_Input(self):
        readObj = Read_Input()

    def Execute_PreGame(self):
        PreGameObj = PreGameSetup()
        PreGameObj.Press_Play()
        PreGameObj.Press_CustomGame()
        PreGameObj.Press_Create()

        PreGameObj.Press_Settings()
        PreGameObj.Press_Preset()
        PreGameObj.Press_Warmup()
        PreGameObj.Press_ApplyPreset()
        PreGameObj.Move_ToSpectator()

        for x in range(0, 4):
            PreGameObj.Press_Invite()
            PreGameObj.Press_BattleTag()
            PreGameObj.Type_PlayerName(x)

        PreGameObj.Press_StartPreGame()

    def ThreadReady1(self):
        ssObj = CMDscreenShots()
        ocrObj = OCR()
        cinObj = CMDinterpreter()
        tsObj = TeamSort()

        while Bridge.AllReady == False:
            with Bridge.ChatBoxSCLock:
                ssObj.ChatBoxScreenShot(1)
            ocrObj.OCRtoText(1)
            ocrObj.OCRtoAnalysis()
            cinObj.OCRAnalysis()
            with Bridge.ChatBoxSCDelLock:
                ssObj.ScreenShotDelete(1)
        Bridge.LimitReady = False

    def ThreadReady2(self):
        ssObj = CMDscreenShots()
        ocrObj = OCR()
        cinObj = CMDinterpreter()

        while Bridge.AllReady == False:
            with Bridge.ChatBoxSCLock:
                ssObj.ChatBoxScreenShot(2)
            ocrObj.OCRtoText(2)
            ocrObj.OCRtoAnalysis()
            cinObj.OCRAnalysis()
            with Bridge.ChatBoxSCDelLock:
                ssObj.ScreenShotDelete(2)
        Bridge.LimitReady = False

    def ThreadReady3(self):
        ssObj = CMDscreenShots()
        ocrObj = OCR()
        cinObj = CMDinterpreter()

        while Bridge.AllReady == False:
            with Bridge.ChatBoxSCLock:
                ssObj.ChatBoxScreenShot(3)
            ocrObj.OCRtoText(3)
            ocrObj.OCRtoAnalysis()
            cinObj.OCRAnalysis()
            with Bridge.ChatBoxSCDelLock:
                ssObj.ScreenShotDelete(3)
        Bridge.LimitReady = False

    def ThreadReady4(self):
        ssObj = CMDscreenShots()
        ocrObj = OCR()
        cinObj = CMDinterpreter()

        while Bridge.AllReady == False:
            with Bridge.ChatBoxSCLock:
                ssObj.ChatBoxScreenShot(4)
            ocrObj.OCRtoText(4)
            ocrObj.OCRtoAnalysis()
            cinObj.OCRAnalysis()
            with Bridge.ChatBoxSCDelLock:
                ssObj.ScreenShotDelete(4)
        Bridge.LimitReady = False

    def ThreadReady5(self):
        ssObj = CMDscreenShots()
        ocrObj = OCR()
        cinObj = CMDinterpreter()

        while Bridge.AllReady == False:
            with Bridge.ChatBoxSCLock:
                ssObj.ChatBoxScreenShot(5)
            ocrObj.OCRtoText(5)
            ocrObj.OCRtoAnalysis()
            cinObj.OCRAnalysis()
            with Bridge.ChatBoxSCDelLock:
                ssObj.ScreenShotDelete(5)
        Bridge.LimitReady = False

    def ThreadReady6(self):
        ssObj = CMDscreenShots()
        ocrObj = OCR()
        cinObj = CMDinterpreter()

        while Bridge.AllReady == False:
            with Bridge.ChatBoxSCLock:
                ssObj.ChatBoxScreenShot(6)
            ocrObj.OCRtoText(6)
            ocrObj.OCRtoAnalysis()
            cinObj.OCRAnalysis()
            with Bridge.ChatBoxSCDelLock:
                ssObj.ScreenShotDelete(6)
        Bridge.LimitReady = False

    def ThreadReady7(self):
        ssObj = CMDscreenShots()
        ocrObj = OCR()
        cinObj = CMDinterpreter()

        while Bridge.AllReady == False:
            with Bridge.ChatBoxSCLock:
                ssObj.ChatBoxScreenShot(7)
            ocrObj.OCRtoText(7)
            ocrObj.OCRtoAnalysis()
            cinObj.OCRAnalysis()
            with Bridge.ChatBoxSCDelLock:
                ssObj.ScreenShotDelete(7)
        Bridge.LimitReady = False

    def Execute_Ready(self):
        # add a multithread solution here.
        # make sure to use allReady as well as locking variables plus maybe queue
        tempList = []
        for x in Bridge.Players:
            tempList.append([x, False])
        Bridge.ReadyPlayers = tempList

        tsObj = TeamSort()
        cmdObj = CMDfunctions()

        ChatThread1 = threading.Thread(target=self.ThreadReady1, args=())   # Threading could cause issues
        ChatThread2 = threading.Thread(target=self.ThreadReady2, args=())
        ChatThread3 = threading.Thread(target=self.ThreadReady3, args=())
        ChatThread4 = threading.Thread(target=self.ThreadReady4, args=())
        ChatThread5 = threading.Thread(target=self.ThreadReady5, args=())
        ChatThread6 = threading.Thread(target=self.ThreadReady6, args=())
        ChatThread7 = threading.Thread(target=self.ThreadReady7, args=())

        ChatThread1.start() # From testing, average time for one tesseract execution is ≈ 0.75 seconds. So seven tess threads each 0.1 appart = much more responsive
        time.sleep(0.1)
        ChatThread2.start()
        time.sleep(0.1)
        ChatThread3.start()
        time.sleep(0.1)
        ChatThread4.start()
        time.sleep(0.1)
        ChatThread5.start()
        time.sleep(0.1)
        ChatThread6.start()
        time.sleep(0.1)
        ChatThread7.start()

        #if Bridge.AllReady == True:
        #   ChatThread1.join()
        #   ChatThread2.join()

        while Bridge.AllReady != True:
            pass

        ChatThread1.join()
        ChatThread2.join()
        ChatThread3.join()
        ChatThread4.join()
        ChatThread5.join()
        ChatThread6.join()
        ChatThread7.join()

        cmdObj.ReadyExecute()
        Bridge.LimitReady = False
        tsObj.Back_ToLobby()

    def Execute_TeamSort(self):
        tsObj = TeamSort()
        tsObj.Take_LobbySlotSC()
        for x in range(0, 2):
            tsObj.Image_ScannerTeam1(x)
        for x in range(2, 4):
            tsObj.Image_ScannerTeam2(x)
        tsObj.Find_Position()
        tsObj.Swap_Logic()
        tsObj.Type_TeamName()

    def Execute_GameStart(self):
        gameObj = PreGameSetup()
        gameObj.Press_StartPreGame()
        keyboard.press(Key.enter)
        time.sleep(0.2)
        keyboard.release(Key.enter)

    def Thread_RP1(self):
        with Bridge.WinnerFLock:
            while Bridge.WinnerFound == False:
                rpObj = ResultProcessing(1)
                TopHalf = threading.Thread(target=rpObj.FirstHalf, args=())
                BottomHalf = threading.Thread(target=rpObj.SecondHalf, args=())

                TopHalf.start()
                BottomHalf.start()
                TopHalf.join()
                BottomHalf.join()

                rpObj.ImageSkew(1)

                with Bridge.WinnerFLock:
                    Bridge.WinnerFound = rpObj.WinnerOCR()

    def Thread_RP2(self):
        with Bridge.WinnerFLock:
            while Bridge.WinnerFound == False:
                rpObj = ResultProcessing(2)
                TopHalf = threading.Thread(target=rpObj.FirstHalf, args=())
                BottomHalf = threading.Thread(target=rpObj.SecondHalf, args=())

                TopHalf.start()
                BottomHalf.start()
                TopHalf.join()
                BottomHalf.join()

                rpObj.ImageSkew(2)

                with Bridge.WinnerFLock:
                    Bridge.WinnerFound = rpObj.WinnerOCR()

    def Thread_RP3(self):
        with Bridge.WinnerFLock:
            while Bridge.WinnerFound == False:
                rpObj = ResultProcessing(3)
                TopHalf = threading.Thread(target=rpObj.FirstHalf, args=())
                BottomHalf = threading.Thread(target=rpObj.SecondHalf, args=())

                TopHalf.start()
                BottomHalf.start()
                TopHalf.join()
                BottomHalf.join()

                rpObj.ImageSkew(3)

                with Bridge.WinnerFLock:
                    Bridge.WinnerFound = rpObj.WinnerOCR()

    def Thread_RP4(self):
        with Bridge.WinnerFLock:
            while Bridge.WinnerFound == False:
                rpObj = ResultProcessing(4)
                TopHalf = threading.Thread(target=rpObj.FirstHalf, args=())
                BottomHalf = threading.Thread(target=rpObj.SecondHalf, args=())

                TopHalf.start()
                BottomHalf.start()
                TopHalf.join()
                BottomHalf.join()

                rpObj.ImageSkew(4)

                with Bridge.WinnerFLock:
                    Bridge.WinnerFound = rpObj.WinnerOCR()

    def Thread_RP5(self):
        with Bridge.WinnerFLock:
            while Bridge.WinnerFound == False:
                rpObj = ResultProcessing(5)
                TopHalf = threading.Thread(target=rpObj.FirstHalf, args=())
                BottomHalf = threading.Thread(target=rpObj.SecondHalf, args=())

                TopHalf.start()
                BottomHalf.start()
                TopHalf.join()
                BottomHalf.join()

                rpObj.ImageSkew(5)

                with Bridge.WinnerFLock:
                    Bridge.WinnerFound = rpObj.WinnerOCR()

    def Thread_RP6(self):
        with Bridge.WinnerFLock:
            while Bridge.WinnerFound == False:
                rpObj = ResultProcessing(6)
                TopHalf = threading.Thread(target=rpObj.FirstHalf, args=())
                BottomHalf = threading.Thread(target=rpObj.SecondHalf, args=())

                TopHalf.start()
                BottomHalf.start()
                TopHalf.join()
                BottomHalf.join()

                rpObj.ImageSkew(6)

                with Bridge.WinnerFLock:
                    Bridge.WinnerFound = rpObj.WinnerOCR()

    def Thread_RP7(self):
        with Bridge.WinnerFLock:
            while Bridge.WinnerFound == False:
                rpObj = ResultProcessing(7)
                TopHalf = threading.Thread(target=rpObj.FirstHalf, args=())
                BottomHalf = threading.Thread(target=rpObj.SecondHalf, args=())

                TopHalf.start()
                BottomHalf.start()
                TopHalf.join()
                BottomHalf.join()

                rpObj.ImageSkew(7)

                with Bridge.WinnerFLock:
                    Bridge.WinnerFound = rpObj.WinnerOCR()

    def Execute_Result_Processing(self):
        RP_thread1 = threading.Thread(target=self.Thread_RP1, args=(), daemon=True) # Idk if this should be daemon=True
        RP_thread2 = threading.Thread(target=self.Thread_RP2, args=(), daemon=True)
        RP_thread3 = threading.Thread(target=self.Thread_RP3, args=(), daemon=True)
        RP_thread4 = threading.Thread(target=self.Thread_RP4, args=(), daemon=True)
        RP_thread5 = threading.Thread(target=self.Thread_RP5, args=(), daemon=True)
        RP_thread6 = threading.Thread(target=self.Thread_RP6, args=(), daemon=True)
        RP_thread7 = threading.Thread(target=self.Thread_RP7, args=(), daemon=True)

        RP_thread1.start()
        time.sleep(0.1)
        RP_thread2.start()
        time.sleep(0.1)
        RP_thread3.start()
        time.sleep(0.1)
        RP_thread4.start()
        time.sleep(0.1)
        RP_thread5.start()
        time.sleep(0.1)
        RP_thread6.start()
        time.sleep(0.1)
        RP_thread7.start()

        while Bridge.WinnerFound == False:
            pass

        RP_thread1.join()
        RP_thread2.join()
        RP_thread3.join()
        RP_thread4.join()
        RP_thread5.join()
        RP_thread6.join()
        RP_thread7.join()

    def Thread_InGameCmd1(self):
        cmdSCObj = CMDscreenShots()
        ocrObj = OCR()
        cmdObj = CMDinterpreter()

        '''tempList = []
        for x in Bridge.Players:
            tempList.append([x, False])
        Bridge.ForfeitPlayers = tempList
        
        This is weird, it showed up in the other thread functions made in this class. It was already defined there once, but if any issues try messing around with this
        Not weird, just didn't see the ForfeitPlayers parts 
        '''

        while Bridge.WinnerFound == False:
            cmdSCObj.InBetweenRounds(8)
            between_rounds = ocrObj.BetweenRounds_Check(8)
            cmdSCObj.Delete_InBetweenRounds(8)
            if between_rounds == False:
                cmdSCObj.ChatBoxScreenShot(8)
                ocrObj.OCRtoText(8)
                ocrObj.OCRtoAnalysis()
                cmdObj.OCRAnalysis()
                cmdSCObj.ScreenShotDelete(8)

    def Thread_InGameCmd2(self):
        cmdSCObj = CMDscreenShots()
        ocrObj = OCR()
        cmdObj = CMDinterpreter()

        '''tempList = []
        for x in Bridge.Players:
            tempList.append([x, False])
        Bridge.ForfeitPlayers = tempList'''

        while Bridge.WinnerFound == False:
            cmdSCObj.InBetweenRounds(9)
            between_rounds = ocrObj.BetweenRounds_Check(9)
            cmdSCObj.Delete_InBetweenRounds(9)
            if between_rounds == False:
                cmdSCObj.ChatBoxScreenShot(9)
                ocrObj.OCRtoText(9)
                ocrObj.OCRtoAnalysis()
                cmdObj.OCRAnalysis()
                cmdSCObj.ScreenShotDelete(9)

    def Thread_InGameCmd3(self):
        cmdSCObj = CMDscreenShots()
        ocrObj = OCR()
        cmdObj = CMDinterpreter()

        while Bridge.WinnerFound == False:
            cmdSCObj.InBetweenRounds(10)
            between_rounds = ocrObj.BetweenRounds_Check(10)
            cmdSCObj.Delete_InBetweenRounds(10)
            if between_rounds == False:
                cmdSCObj.ChatBoxScreenShot(10)
                ocrObj.OCRtoText(10)
                ocrObj.OCRtoAnalysis()
                cmdObj.OCRAnalysis()
                cmdSCObj.ScreenShotDelete(10)

    def Thread_InGameCmd4(self):
        cmdSCObj = CMDscreenShots()
        ocrObj = OCR()
        cmdObj = CMDinterpreter()

        while Bridge.WinnerFound == False:
            cmdSCObj.InBetweenRounds(11)
            between_rounds = ocrObj.BetweenRounds_Check(11)
            cmdSCObj.Delete_InBetweenRounds(11)
            if between_rounds == False:
                cmdSCObj.ChatBoxScreenShot(11)
                ocrObj.OCRtoText(11)
                ocrObj.OCRtoAnalysis()
                cmdObj.OCRAnalysis()
                cmdSCObj.ScreenShotDelete(11)

    def Thread_InGameCmd5(self):
        cmdSCObj = CMDscreenShots()
        ocrObj = OCR()
        cmdObj = CMDinterpreter()

        while Bridge.WinnerFound == False:
            cmdSCObj.InBetweenRounds(12)
            between_rounds = ocrObj.BetweenRounds_Check(12)
            cmdSCObj.Delete_InBetweenRounds(12)
            if between_rounds == False:
                cmdSCObj.ChatBoxScreenShot(12)
                ocrObj.OCRtoText(12)
                ocrObj.OCRtoAnalysis()
                cmdObj.OCRAnalysis()
                cmdSCObj.ScreenShotDelete(12)

    def Thread_InGameCmd6(self):
        cmdSCObj = CMDscreenShots()
        ocrObj = OCR()
        cmdObj = CMDinterpreter()

        while Bridge.WinnerFound == False:
            cmdSCObj.InBetweenRounds(13)
            between_rounds = ocrObj.BetweenRounds_Check(13)
            cmdSCObj.Delete_InBetweenRounds(13)
            if between_rounds == False:
                cmdSCObj.ChatBoxScreenShot(13)
                ocrObj.OCRtoText(13)
                ocrObj.OCRtoAnalysis()
                cmdObj.OCRAnalysis()
                cmdSCObj.ScreenShotDelete(13)

    def Thread_InGameCmd7(self):
        cmdSCObj = CMDscreenShots()
        ocrObj = OCR()
        cmdObj = CMDinterpreter()

        while Bridge.WinnerFound == False:
            cmdSCObj.InBetweenRounds(14)
            between_rounds = ocrObj.BetweenRounds_Check(14)
            cmdSCObj.Delete_InBetweenRounds(14)
            if between_rounds == False:
                cmdSCObj.ChatBoxScreenShot(14)
                ocrObj.OCRtoText(14)
                ocrObj.OCRtoAnalysis()
                cmdObj.OCRAnalysis()
                cmdSCObj.ScreenShotDelete(14)

    def Execute_InGameCommands(self):
        tempList = []
        for x in Bridge.Players:
            tempList.append([x, False])
        Bridge.ForfeitPlayers = tempList

        IGCMD1 = threading.Thread(target=self.Thread_InGameCmd1, args=(), daemon=True)  # daemon=True might not be needed
        IGCMD2 = threading.Thread(target=self.Thread_InGameCmd2, args=(), daemon=True)
        IGCMD3 = threading.Thread(target=self.Thread_InGameCmd3, args=(), daemon=True)
        IGCMD4 = threading.Thread(target=self.Thread_InGameCmd4, args=(), daemon=True)
        IGCMD5 = threading.Thread(target=self.Thread_InGameCmd5, args=(), daemon=True)
        IGCMD6 = threading.Thread(target=self.Thread_InGameCmd6, args=(), daemon=True)
        IGCMD7 = threading.Thread(target=self.Thread_InGameCmd7, args=(), daemon=True)

        IGCMD1.start()
        time.sleep(0.1)
        IGCMD2.start()
        time.sleep(0.1)
        IGCMD3.start()
        time.sleep(0.1)
        IGCMD4.start()
        time.sleep(0.1)
        IGCMD5.start()
        time.sleep(0.1)
        IGCMD6.start()
        time.sleep(0.1)
        IGCMD7.start()
        time.sleep(0.1)

        while Bridge.WinnerFound == False:
            pass

        IGCMD1.join()
        IGCMD2.join()
        IGCMD3.join()
        IGCMD4.join()
        IGCMD5.join()
        IGCMD6.join()
        IGCMD7.join()


    def Execute_Results(self):
        rspObj = ResultProcessing() # this will trigger __init__ but should not be a problem
        rspObj.Close_Game()



# class for reading input file
# inputs the .txt file, outputs all of the player names + tags, just player names, teams, and team captains
class Read_Input:
    def __init__(self):
        self.Team1 = []
        self.Team2 = []
        self.Cap1 = ''
        self.Cap2 = ''
        self.playersWTags = []
        self.TotalVotes = [0, 0, 0, 0]
        file = open('2v2Input.txt', 'r')

        for counter, line in enumerate(file):
            if counter == 0:
                fields = line.split(',')
                self.playersWTags = fields[:-1]
            else:
                fields = line.split(',')
                self.TotalVotes = self.AddTwoLists(self.TotalVotes, fields[:-1])

        file.close()
        Bridge.PlayersWithTags = self.playersWTags
        self.players = self.Remove_Tags(self.playersWTags)
        Bridge.Players = self.players
        self.player_votes = zip(self.players, self.TotalVotes)
        self.Make_Teams(self.player_votes)

    def AddTwoLists(self, list1, list2):
        output = []
        list2 = list(map(int, list2))
        for x, y in zip(list1, list2):
            output.append(x + y)

        return output

    def Remove_Tags(self, PlayersWithTags):
        Players = []
        Just_name = ''
        for name in PlayersWithTags:
            for letter in name:
                if letter != '#' and letter != ' ':
                    Just_name = Just_name + letter
                elif letter == '#':
                    break
            Players.append(Just_name)
            Just_name = ''

        return Players

    def Make_Teams(self, Player_Votes):
        in_order = sorted(Player_Votes, key=lambda tup: tup[1])


        for x, y in enumerate(in_order):
            if x % 2 == 0:
                # is even
                self.Team1.append(y[0])
            else:
                # is odd
                self.Team2.append(y[0])

        self.Cap1 = self.Team1[0]
        self.Cap2 = self.Team2[0]
        Bridge.Team1 = self.Team1
        Bridge.Team2 = self.Team2
        Bridge.Cap1 = self.Cap1
        Bridge.Cap2 = self.Cap2

class PreGameSetup:
    def __init__(self):
        self.PlayerList = Bridge.PlayersWithTags

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
        mouse.position = (429, 418) # This was something different for some reason. I think I changed for wrong thing last night
        time.sleep(2)
        mouse.click(Button.left, 1)

    def Press_Warmup(self):
        mouse.position = (400, 400)
        time.sleep(4)
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
        '''keyboard.press(Key.tab)
        time.sleep(0.1)
        keyboard.release(Key.tab)
        time.sleep(0.2)'''

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

    def Press_Invite(self):
        mouse.position = (2150, 400)
        time.sleep(0.13)
        mouse.click(Button.left, 1)
        time.sleep(0.13)

    def Press_BattleTag(self):
        mouse.position = (1550, 410)
        time.sleep(0.16)
        mouse.click(Button.left, 1)
        time.sleep(0.16)

    def Type_PlayerName(self, Number):
        for char in self.PlayerList[Number]:
            if char != ' ':
                keyboard.press(char)
                keyboard.release(char)
                time.sleep(0.1)
        time.sleep(0.1)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        time.sleep(0.1)

class CMDscreenShots:
    def __init__(self):
        pass
        # REMOVED TIME.SLEEP TO SEE IF IT SPEEDS UP THINGS DRASTICALLY -

    def InBetweenRounds(self, SCnum):
        image = pyautogui.screenshot('IntermissionCheck' + str(SCnum) + '.png', region=(901, 201, 763, 129))

    def Delete_InBetweenRounds(self, SCnum):
        os.remove('IntermissionCheck' + str(SCnum) + '.png')

    def ChatBoxScreenShot(self, SCnum):
        #time.sleep(0.5)
        image = pyautogui.screenshot('BlinkCommandSC' + str(SCnum) + '.png', region=(53, 804, 531, 150)) # region changes depending on whether it is in lobby: (0, 1000, 640, 380)    160 WAS 120!!
        #time.sleep(0.5)

    def ScreenShotDelete(self, SCnum):
        #time.sleep(0.5)
        os.remove('BlinkCommandSC' + str(SCnum) + '.png')

class OCR:
    def __init__(self):
        self.text = ''
        self.textArray = []

    def BetweenRounds_Check(self, SCnum):
        image = Image.open('IntermissionCheck' + str(SCnum) + '.png')
        text = pytesseract.image_to_string(image, lang='eng')

        text_ratio = fuzz.ratio(text, 'ROUND COMPLETE')

        if text_ratio > 60:
            return True # We are in the intermission of rounds
        else:
            return False # We are not in the intermission of rounds

    def OCRtoText(self, SCnum):
        image = Image.open('BlinkCommandSC' + str(SCnum) + '.png')
        text = pytesseract.image_to_string(image, lang='eng')
        self.text = text

    def OCRtoAnalysis(self):
        output = []
        tempString = ''
        for char in self.text:
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
        self.textArray = output
        Bridge.text_Array = self.textArray

class CMDinterpreter:
    def __init__(self):
        pass

    def CMDswitch(self, cmdCode, playername):
        cmdObj = CMDfunctions()
        if cmdCode == 0:
            # call ready function[s]
            cmdObj.ReadyTracker(playername)
        elif cmdCode == 1:
            # call pause function[s]
            with Bridge.PauseLock:
                if Bridge.PauseState == False:
                    cmdObj.Pause()
                    Bridge.PauseState = True
        elif cmdCode == 2:
            # call unpause function[s]
            with Bridge.PauseLock:
                if Bridge.PauseState == True:
                    cmdObj.Unpause()
                    Bridge.PauseState = False
        elif cmdCode == 3:
            # call unready function[s]
            pass
        elif cmdCode == 4:
            # call readystatus function[s]
            cmdObj.ReadyStatus()
        elif cmdCode == 5:
            # call forfeit function[s]
            pass
        elif cmdCode == 6:
            # call cmds function[s]
            pass

    def OCRAnalysis(self):
        ChatStringArray = Bridge.text_Array

        if len(ChatStringArray) > 0:
            print(ChatStringArray)
            maxIndex = len(ChatStringArray)
            ChatString = ChatStringArray[maxIndex - 1] # either 0 or max - just need last line of text from chat

            nameString = ''
            nameRecording = None
            nameCounter = 0
            for x in range(0, len(ChatString)):
                testChar = ChatString[x]

                if nameRecording:  # == True
                    nameString = nameString + testChar
                    nameCounter = nameCounter + 1

                if testChar == '[' or testChar == '(':  # Added curved brackets because OCR sucks
                    nameRecording = True

                if nameCounter > 12:
                    break

                if testChar == ']' or testChar == ')':
                    nameString = nameString[:-1]
                    break

            print(nameString)
            name_match = []
            for name in Bridge.Players:
                name_match.append(fuzz.ratio(nameString, name))

            highest_name_match = max(name_match)
            name_index = name_match.index(highest_name_match)

            if highest_name_match > 85:
                nameString = Bridge.Players[name_index]

            print(nameString)
            validName = nameString in Bridge.Players

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

                print(commandString)

                cmd_match = []
                for cmd in Bridge.Commands:
                    cmd_match.append(fuzz.ratio(commandString, cmd))

                highest_cmd_match = max(cmd_match)
                cmd_index = cmd_match.index(highest_cmd_match)

                if highest_cmd_match > 85:
                    commandString = Bridge.Commands[cmd_index]

                print(commandString)

                if commandString in Bridge.Commands:
                    cmdPosition = Bridge.Commands.index(commandString)
                    print(commandString)
                    if Bridge.LimitReady == True:
                        if cmdPosition == 0 or cmdPosition == 4:
                            self.CMDswitch(cmdPosition, nameString)
                    else:
                        if cmdPosition != 0 and cmdPosition != 4:
                            self.CMDswitch(cmdPosition, nameString)
                else:
                    pass
            else:
                pass

class CMDfunctions:
    def __init__(self):
        pass

    def ReadyExecute(self):
        matchReadyMessage1 = "ALL PLAYERS READY ~~~ MATCH WILL BE LIVE SOON"
        '''keyboard.press(Key.enter)
        time.sleep(0.02)
        keyboard.press(Key.enter)
        time.sleep(0.02)'''
        time.sleep(3)
        #Bridge.AllReady = True
        #Bridge.LimitReady = False
        for char in matchReadyMessage1:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.08)
        keyboard.press(Key.enter)
        time.sleep(0.02)
        keyboard.press(Key.enter)
        time.sleep(0.02)

    def ReadyTracker(self, name):
        # searches Players for the position and changes the False to True in ReadyPlayers
        # Get this to work and get PyCharm to work with main source code
        player_pos = Bridge.Players.index(name)
        print(Bridge.ReadyPlayers)
        Bridge.ReadyPlayers[player_pos] = [name, True]
        print(Bridge.ReadyPlayers)

        readyCheck = True
        for q in range(0, len(Bridge.ReadyPlayers)):
            if Bridge.ReadyPlayers[q][1] == False:
                readyCheck = False
                break
                # could break, but this might be good for readystatus - probably no

        #if readyCheck == True:
        #    self.ReadyExecute()

        if readyCheck == True:
            Bridge.AllReady = True
            Bridge.LimitReady = False

    def ReadyStatus(self):
        if Bridge.LastRS != -1:
            with Bridge.TimeLock:
                Bridge.timerCheck = int(round(time.time() - Bridge.LastRS))

        if Bridge.LastRS == -1 or Bridge.timerCheck > Bridge.RS_TIMER:
            with Bridge.LastRSLock:
                Bridge.LastRS = time.time()

            tempList = []
            for x, y in enumerate(Bridge.ReadyPlayers):
                if Bridge.ReadyPlayers[x][1] == False:
                    tempList.append(Bridge.ReadyPlayers[x][0])

            typeoutput = str(tempList)
            print(typeoutput)


            for char in typeoutput:
                keyboard.press(char)
                time.sleep(0.02)
                keyboard.release(char)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
            time.sleep(0.2)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)

    def Pause(self):                    # sort this out
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.1)
        keyboard.press(Key.ctrl_l)
        time.sleep(0.1)
        keyboard.press(Key.shift_l)
        time.sleep(0.1)
        keyboard.press('=')
        time.sleep(0.1)

        keyboard.release(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.ctrl_l)
        time.sleep(0.1)
        keyboard.release(Key.shift_l)
        time.sleep(0.1)
        keyboard.release('=')
        time.sleep(0.1)

        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        #  NO CHECK TO STOP PEOPLE USING PAUSE WHILST GAME IS PAUSED. ALSO, NOT VOTE TO KEEP TRACK LIKE AT LEAST THREE PEOPLE NEED TO VOTE YOU KNOW
        TypeString = "Game has been paused! To unpause type \"unpause\" in command form (%%)!"
        for char in TypeString:
            keyboard.press(char)
            time.sleep(0.1)
            keyboard.release(char)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        time.sleep(0.2)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        time.sleep(0.1)

    def Unpause(self):
        time.sleep(0.1)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        time.sleep(0.1)
        keyboard.press(Key.ctrl_l)
        time.sleep(0.1)
        keyboard.press(Key.shift_l)
        time.sleep(0.1)
        keyboard.press('=')
        time.sleep(0.1)

        keyboard.release(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.ctrl_l)
        time.sleep(0.1)
        keyboard.release(Key.shift_l)
        time.sleep(0.1)
        keyboard.release('=')
        time.sleep(0.1)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        time.sleep(0.1)

        TypeString = "Game is set to unpause!"
        for char in TypeString:
            keyboard.press(char)
            time.sleep(0.1)
            keyboard.release(char)
        time.sleep(0.1)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        time.sleep(0.2)
        keyboard.press(Key.enter)
        time.sleep(0.1)
        keyboard.release(Key.enter)
        time.sleep(0.1)

    def Forfeit(self, name):                    # THIS IS NOT DONE PROPERLY
        player_pos = Bridge.Players.index(name)
        print(Bridge.ForfeitPlayers)
        Bridge.ForfeitPlayers[player_pos] = [name, True]
        print(Bridge.ReadyPlayers)

        readyCheck = True
        for q in range(0, len(Bridge.ReadyPlayers)):
            if Bridge.ReadyPlayers[q][1] == False:
                readyCheck = False
                break
                # could break, but this might be good for readystatus - probably no

        if readyCheck == True:
            self.ReadyExecute()

class TeamSort:
    def __init__(self):
        self.Players = Bridge.Players
        self.Team1 = Bridge.Team1
        self.Team2 = Bridge.Team2
        self.Captain1 = Bridge.Cap1
        self.Captain2 = Bridge.Cap2

        self.CorrectPos = []  # This contains the name of each player as well as whether they are on the correct team or not
        self.CurrentPos = []

        self.SortTuples = [(441, 634), (441, 715), (1338, 640), (1338, 717)]   # first 6 are team 1, last 6 are team 2

        for x in Bridge.Team1:  # This fills this list out
            self.CorrectPos.append([x, 1])  # This doesn't work

        for x in Bridge.Team2:
            self.CorrectPos.append([x, 2])

    def Back_ToLobby(self):
        # Text chat should be closed.
        time.sleep(4)
        keyboard.press(Key.enter)
        time.sleep(0.2)
        keyboard.release(Key.enter)
        time.sleep(0.1)

        keyboard.press(Key.esc)
        time.sleep(0.1)
        keyboard.release(Key.esc)
        time.sleep(0.1)

        mouse.position = (1280, 720)
        time.sleep(0.1)
        mouse.click(Button.left, 1)
        time.sleep(0.1)

        pgsObj = PreGameSetup()
        pgsObj.Press_Settings()
        pgsObj.Press_Preset()

        time.sleep(0.2)
        mouse.position = (1600, 480)
        time.sleep(2)
        mouse.click(Button.left, 1)
        time.sleep(0.04)
        mouse.position = (1366, 852)
        time.sleep(0.2)
        mouse.click(Button.left, 1)
        time.sleep(3)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(0.2)
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        time.sleep(0.2)
        mouse.position = (1023, 1225)
        time.sleep(0.2)
        mouse.click(Button.left, 1)
        time.sleep(0.2)

    def Take_LobbySlotSC(self):
        # This will take 12 screenshots of the players in the lobby slots
        time.sleep(3)
        for x in range(0, 2):
            image = pyautogui.screenshot('LobbySlotSC' + str(x) + '.png', region=(68, 600 + x * 82, 639, 75))
        for x in range(0, 2):
            image = pyautogui.screenshot('LobbySlotSC' + str(x + 2) + '.png', region=(1072, 600 + x * 82, 639, 75))     # < THIS IS REALLY ANNOYING!

    def Delete_ScreenShots(self):
        for x in range(0, 4):
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

        image.crop((max(bronze_xTracker), 0, width, height)).save('LobbySlotSC' + str(imageNum) + '.png') # don't know if this will work - I do want it to overwrite the existing file tho

    def Image_ScannerTeam2(self, imageNum):
        image = Image.open('LobbySlotSC' + str(imageNum) + '.png')
        width, height = image.size
        rgb_image = image.convert('RGB')

        bronze_xTracker = []

        for y in range(0, height):
            for x in range(0, width):
                r, g, b = rgb_image.getpixel((x, y))

                if r > 160 and r < 180 and g > 90 and g < 110 and b > 60 and b < 80:
                    bronze_xTracker.append(x)

        image.crop((0, 0, min(bronze_xTracker), height)).save('LobbySlotSC' + str(imageNum) + '.png')

    def Find_Position(self):
        match_ratios = []
        highest_ratios = []
        for x in range(0, 4):
            image = Image.open('LobbySlotSC' + str(x) + '.png')
            text = pytesseract.image_to_string(image, lang='eng')
            # text is now the name of the player
            # if <6, team 1, >6, team 2
            for name in self.Players:
                match_ratios.append(fuzz.ratio(text, name))

            highest_ratios.append(match_ratios.index(max(match_ratios)))

            if x < 2:
                self.CurrentPos.append([self.Players[highest_ratios[x]], 1])
                match_ratios = []
            else:
                self.CurrentPos.append([self.Players[highest_ratios[x]], 2])
                match_ratios = []


    def Swap(self, pos1, pos2):

        for x in range(0, 4):
            if pos1 == x:
                mouse.position = self.SortTuples[x]
                time.sleep(0.02)
                mouse.click(Button.left, 1)

                for y in range(0, 4):
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
                        if x < 2:                                                # THIS PROBS DOESNT WORK. TRY AND ELSE
                            incorrectPosTeam1.append([self.CurrentPos[x][0], x])
                        else:   # this is new
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

class ResultProcessing: # fix this
    def __init__(self, SCnum):
        # port over winnTestingMultithread to here. Make it take the screen shot and store the other parameters in here
        # so that other functions can use the shared variables.
        self.image = pyautogui.screenshot('WinnerCheck' + str(SCnum) + '.png', region=(224, 558, 2107, 314))
        self.pixels = self.image.load()
        self.image2 = self.image # this is just a place holder
        self.image3 = self.image # this too
        self.image4 = self.image

    def FirstHalf(self):
        width, height = self.image.size

        for x in range(0, width):
            for y in range(0, int(round(height / 2))):
                r, g, b, a = self.pixels[x, y]

                if (r <= 255 and r > 240 and g <= 225 and g >= 215 and b <= 88 and b >= 78):
                    self.pixels[x, y] = (0, 0, 0)
                else:
                    self.pixels[x, y] = (255, 255, 255)

    def SecondHalf(self):
        width, height = self.image.size

        for x in range(0, width):
            for y in range(int(round(height / 2)), height):
                r, g, b, a = self.pixels[x, y]

                if (r <= 255 and r > 240 and g <= 225 and g >= 215 and b <= 88 and b >= 78):
                    self.pixels[x, y] = (0, 0, 0)
                else:
                    self.pixels[x, y] = (255, 255, 255)

    def ImageSkew(self, SCnum):
        self.image.save('BlackOutTest' + str(SCnum) + '.png')
        self.image2 = Image.open('BlackOutTest' + str(SCnum) + '.png')

        width, height = self.image2.size
        m = -0.259
        xshift = abs(m) * width
        new_width = width + int(round(xshift))
        img = self.image2.transform((new_width, height), Image.AFFINE,
                               (1, m, -xshift if m > 0 else 0, 0, 1, 0), Image.BICUBIC)
        img.save('BlackOutSkewTest' + str(SCnum) + '.png')

        img.crop((70, 22, 2104, 274)).save('WinnerPreOCR' + str(SCnum) + '.png')

        self.image3 = Image.open('WinnerPreOCR' + str(SCnum) + '.png')
        self.image3.resize((3100, 252)).save('WinnerPreOCRStretched' + str(SCnum) + '.png')

        self.image4 = Image.open('WinnerPreOCRStretched' + str(SCnum) + '.png')

    def WinnerOCR(self):
        text = pytesseract.image_to_string(self.image4, lang='eng')

        Upper_Cap1 = Bridge.Cap1[:1].upper() + Bridge.Cap1[1:]
        Upper_Cap2 = Bridge.Cap2[:1].upper() + Bridge.Cap2[1:]


        ratio1 = fuzz.ratio(text, "TEAM " + Upper_Cap1 + " WINS!")
        ratio2 = fuzz.ratio(text, "TEAM " + Upper_Cap2 + " WINS!")

        if ratio1 >= 75 or ratio2 >= 75:
            if ratio1 > ratio2:
                print("team 1 wins!")
                typeString = "TEAM " + Bridge.Cap1 + " WINS!! GGWP! You may leave the lobby now. Lobby will shut down shortly."
                for char in typeString:
                    time.sleep(0.05)
                    keyboard.press(char)
                    time.sleep(0.1)
                    keyboard.release(char)

                time.sleep(0.1)
                keyboard.press(Key.enter)
                time.sleep(0.1)
                keyboard.release(Key.enter)
                return True
            else: # bias towards team 2
                print("team 2 wins!")
                typeString = "TEAM " + Bridge.Cap2 + " WINS!! GGWP! You may leave the lobby now. Lobby will shut down shortly."
                for char in typeString:
                    time.sleep(0.05)
                    keyboard.press(char)
                    time.sleep(0.1)
                    keyboard.release(char)

                time.sleep(0.1)
                keyboard.press(Key.enter)
                time.sleep(0.1)
                keyboard.release(Key.enter)
                return True
        else:
            return False


    def Close_Game(self):
        keyboard.press(Key.esc)
        keyboard.release(Key.esc)
        mouse.position = (1280, 720)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        time.sleep(0.1)
        mouse.position = (1019, 1226)
        time.sleep(0.3)
        mouse.position = (1407, 1218)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        mouse.position = (1350, 720)
        time.sleep(0.3)
        mouse.click(Button.left, 1)
        mouse.position = (1280, 720)
        print("FINISHED")

 


exe = Execute_Order()
ResultProcess = multiprocessing.Process(target=exe.Execute_Result_Processing, args=())  # this is multiprocesed, was threaded idk if it will work well
CMDProcess = multiprocessing.Process(target=exe.Execute_InGameCommands, args=()) # when this was thread, it was daemon, now it is different
### COMMAND ZONE
exe.Execute_Read_Input()
exe.Execute_PreGame()
exe.Execute_Ready()
exe.Execute_TeamSort()
exe.Execute_GameStart()
ResultProcess.start()
CMDProcess.start()
if Bridge.WinnerFound == True:
    ResultProcess.join()
    CMDProcess.join()
exe.Execute_Results()
### COMMAND ZONE


