from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from PIL import Image
import time
import pyautogui
import os
import pytesseract
from fuzzywuzzy import fuzz

def Make_Teams(Player_Votes):
    in_order = sorted(Player_Votes, key=lambda tup: tup[1])
    Team1 = []
    Team2 = []

    for x, y in enumerate(in_order):
        if x % 2 == 0:
            # is even
            Team1.append(y[0])
        else:
            # is odd
            Team2.append(y[0])

    Cap1 = Team1[0]
    Cap2 = Team2[0]

    print(Team1)
    print(Team2)

def Remove_Tags(PlayersWithTags):
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

def AddTwoLists(list1, list2):
    output = []
    list2 = list(map(int, list2))
    for x, y in zip(list1, list2):
        output.append(x + y)

    return output

def FileReader():
    playersWTags = []
    TotalVotes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    file = open('BlinkInput.txt', 'r')

    for counter, line in enumerate(file):
        if counter == 0:
            fields = line.split(',')
            playersWTags = fields[:-1]
        else:
            fields = line.split(',')
            TotalVotes = AddTwoLists(TotalVotes, fields[:-1])

    file.close()

    players = Remove_Tags(playersWTags)

    player_votes = zip(players, TotalVotes)
    Make_Teams(player_votes)





FileReader()
