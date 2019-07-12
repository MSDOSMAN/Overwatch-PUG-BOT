correctPos = [['EASY ANA', 1], ['EASY BASTION', 1], ['EASY LÚCIO', 1], ['EASY MCCREE', 1], ['EASY ROADHOG', 1], ['EASY REAPER', 1], ['EASY MEI', 2], ['EASY SOLDIER:76', 2], ['EASY SOMBRA', 2], ['EASY TORBJÖRN', 2], ['EASY ZARYA', 2], ['EASY ZENYATTA', 2]]
currentPos = [['EASY MEI', 1], ['EASY BASTION', 1], ['EASY LÚCIO', 2], ['EASY MCCREE', 1], ['EASY ROADHOG', 1], ['EASY REAPER', 1], ['EASY ANA', 2], ['EASY SOMBRA', 1], ['EASY SOLDIER:76', 2], ['EASY TORBJÖRN', 2], ['EASY ZARYA', 2], ['EASY ZENYATTA', 2]]

incorrectPosTeam1 = []
incorrectPosTeam2 = []

for x in range(0, len(currentPos)):
    for y in range(0, len(correctPos)):
        if currentPos[x][0] == correctPos[y][0]:
            if currentPos[x][1] != correctPos[y][1]:
                if x < 6:
                    incorrectPosTeam1.append([currentPos[x][0], x])
                elif x > 5:
                    incorrectPosTeam2.append([currentPos[x][0], x])



for z in range(0, len(incorrectPosTeam1)):
    print("Swap: " + str(incorrectPosTeam1[z][1]) + ", " + str(incorrectPosTeam2[z][1]))



