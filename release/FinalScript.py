from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from PIL import Image
import time
import pyautogui
import os
import pytesseract
from fuzzywuzzy import fuzz
import threading

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
    Commands = ['ready', 'pause', 'unpause', 'unready', 'readystatus', 'forfeit']
    TimeSinceRStatus = -1
    WinnerFound = False
    ForfeitPlayers = []

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

        for x in range(0, 12):
            PreGameObj.Press_Invite()
            PreGameObj.Press_BattleTag()
            PreGameObj.Type_PlayerName(x)

        PreGameObj.Press_StartPreGame()

    def Execute_Ready(self):
        ssObj = CMDscreenShots()
        ocrObj = OCR()
        cinObj = CMDinterpreter()


        tempList = []
        for x in Bridge.Players:
            tempList.append([x, False])
        Bridge.ReadyPlayers = tempList

        while Bridge.AllReady == False:
            ssObj.ChatBoxScreenShot()
            ocrObj.OCRtoText()
            ocrObj.OCRtoAnalysis()
            cinObj.OCRAnalysis()
            ssObj.ScreenShotDelete()
        Bridge.LimitReady = False

    def Execute_TeamSort(self):
        tsObj = TeamSort()
        tsObj.Take_LobbySlotSC()
        for x in range(0, 6):
            tsObj.Image_ScannerTeam1(x)
        for x in range(6, 12):
            tsObj.Image_ScannerTeam2(x)
        tsObj.Find_Position()
        tsObj.Swap_Logic()
        tsObj.Type_TeamName()

    def Execute_GameStart(self):
        gameObj = PreGameSetup()
        gameObj.Press_StartPreGame()
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    def Execute_Result_Processing(self):
        rpObj = ResultProcessing()
        while Bridge.WinnerFound == False:
            Bridge.WinnerFound = rpObj.WinnerProcessing(rpObj.WinnerScreenShot())
            if Bridge.WinnerFound == False:
                rpObj.WinnerScreenShotDelete()

    def Execute_InGameCommands(self):
        cmdSCObj = CMDscreenShots()
        ocrObj = OCR()
        cmdObj = CMDinterpreter()

        tempList = []
        for x in Bridge.Players:
            tempList.append([x, False])
        Bridge.ForfeitPlayers = tempList

        while Bridge.WinnerFound == False:
            cmdSCObj.ChatBoxScreenShot()
            ocrObj.OCRtoText()
            ocrObj.OCRtoAnalysis()
            cmdObj.OCRAnalysis()

    def Execute_Results(self):
        rspObj = ResultProcessing()
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
        self.TotalVotes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        file = open('RealInput.txt', 'r')

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
        mouse.position = (300, 350)
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

    def ChatBoxScreenShot(self):
        time.sleep(0.5)
        image = pyautogui.screenshot('BlinkCommandSC.png', region=(29, 597, 571, 334)) # region changes depending on whether it is in lobby: (0, 1000, 640, 380)
        time.sleep(0.5)

    def ScreenShotDelete(self):
        time.sleep(0.5)
        os.remove('BlinkCommandSC.png')

class OCR:
    def __init__(self):
        self.text = ''
        self.textArray = []

    def OCRtoText(self):
        image = Image.open('BlinkCommandSC.png')
        text = pytesseract.image_to_string(image, lang='eng')
        self.text = text

    def OCRtoAnalysis(self):
        output = []
        tempString = ''
        for char in self.text:
            tempString = tempString + char
            if char == '\n':
                output.append(
                    tempString[
                    :-1])  # [:-1] will remove the \n at the end of the statement. This could be useful however
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
            cmdObj.Pause()
        elif cmdCode == 2:
            # call unpause function[s]
            cmdObj.Unpause()
        elif cmdCode == 3:
            # call unready function[s]
            pass
        elif cmdCode == 4:
            # call readystatus function[s]
            cmdObj.ReadyStatus()
            pass
        elif cmdCode == 5:
            # call forfeit function[s]
            pass

    def OCRAnalysis(self):
        ChatStringArray = Bridge.text_Array

        if len(ChatStringArray) > 0:
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

                if testChar == '[':
                    nameRecording = True

                if nameCounter > 12:
                    break

                if testChar == ']':
                    nameString = nameString[:-1]
                    break

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
                    None
            else:
                None

class CMDfunctions:
    def __init__(self):
        pass

    def ReadyExecute(self):
        matchReadyMessage1 = "ALL PLAYERS READY ~~~ MATCH WILL BE LIVE SOON"
        time.sleep(3)
        Bridge.AllReady = True
        Bridge.LimitReady = False
        for char in matchReadyMessage1:
            keyboard.press(char)
            keyboard.release(char)
            time.sleep(0.08)

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

        if readyCheck == True:
            self.ReadyExecute()


    def ReadyStatus(self):
        if Bridge.TimeSinceRStatus != -1:
            time_check = time.time() - Bridge.TimeSinceRStatus
        if Bridge.TimeSinceRStatus == -1 or time_check > 10:
            Bridge.TimeSinceRStatus = time.time()
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

    def Pause(self):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press('=')

        keyboard.release(Key.enter)
        keyboard.release(Key.ctrl_l)
        keyboard.release(Key.shift_l)
        keyboard.release('=')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        #  NO CHECK TO STOP PEOPLE USING PAUSE WHILST GAME IS PAUSED. ALSO, NOT VOTE TO KEEP TRACK LIKE AT LEAST THREE PEOPLE NEED TO VOTE YOU KNOW
        TypeString = "Game has been paused! To unpause type \"unpause\" in command form (%%)!"
        for char in TypeString:
            keyboard.press(char)
            time.sleep(0.2)
            keyboard.release(char)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    def Unpause(self):
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        keyboard.press(Key.ctrl_l)
        keyboard.press(Key.shift_l)
        keyboard.press('=')

        keyboard.release(Key.enter)
        keyboard.release(Key.ctrl_l)
        keyboard.release(Key.shift_l)
        keyboard.release('=')
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        TypeString = "Game is set to unpause!"
        for char in TypeString:
            keyboard.press(char)
            time.sleep(0.2)
            keyboard.release(char)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(0.2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

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

        self.SortTuples = [(441, 634), (441, 715), (441, 795), (441, 888), (441, 967), (441, 1041), (1338, 640), (1338, 717), (1338, 798), (1338, 882), (1338, 961), (1338, 1039)]   # first 6 are team 1, last 6 are team 2

        for x in Bridge.Team1:  # This fills this list out
            self.CorrectPos.append([x, 1])  # This doesn't work

        for x in Bridge.Team2:
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

                if r > 210 and r < 230 and g > 145 and g < 160 and b > 120 and b < 140:
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

                if r > 210 and r < 230 and g > 145 and g < 160 and b > 120 and b < 140:
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

class ResultProcessing:
    def __init__(self):
        pass

    def WinnerScreenShot(self):
        image = pyautogui.screenshot('WinnerScreen.png', region=(751, 1314, 146, 46))
        image2 = Image.open('WinnerScreen.png')
        text = pytesseract.image_to_string(image2, lang='eng')
        print(text)
        return text

    def WinnerScreenShotDelete(self):
        os.remove('WinnerScreen.png')

    def WinnerProcessing(self, text):
        match_ratios_team1 = []
        match_ratios_team2 = []

        for x in Bridge.Team1:
            match_ratios_team1.append(fuzz.ratio(text, x))
        for y in Bridge.Team2:
            match_ratios_team2.append(fuzz.ratio(text, y))

        if max(match_ratios_team1) > 50 or max(match_ratios_team2) > 50:
            if max(match_ratios_team1) > max(match_ratios_team2):
                # player from team 1 detected, so team 2 won
                print("team 2 wins!")
                typeString = "TEAM " + Bridge.Cap2 + " WINS!! GGWP! You may leave the lobby now. Lobby will shut down shortly."
                for char in typeString:
                    keyboard.press(char)
                    time.sleep(0.2)
                    keyboard.release(char)

                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                return True
            else:
                print("team 1 wins!")
                typeString = "TEAM " + Bridge.Cap1 + " WINS!! GGWP! You may leave the lobby now. Lobby will shut down shortly."
                for char in typeString:
                    keyboard.press(char)
                    time.sleep(0.2)
                    keyboard.release(char)

                keyboard.press(Key.enter)
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
ResultThread = threading.Thread(target=exe.Execute_Result_Processing, args=())
CMDThread = threading.Thread(target=exe.Execute_InGameCommands, args=())
### COMMAND ZONE
exe.Execute_Read_Input()
exe.Execute_PreGame()
exe.Execute_Ready()
exe.Execute_TeamSort()
exe.Execute_GameStart()
ResultThread.start()
CMDThread.start()
if Bridge.WinnerFound == True:
    ResultThread.join()
    CMDThread.join()
exe.Execute_Results()
### COMMAND ZONE


