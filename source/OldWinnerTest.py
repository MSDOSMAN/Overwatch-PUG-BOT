def __init__(self):
    pass


def WinnerScreenShot(self):
    image = pyautogui.screenshot('WinnerScreen.png', region=(1180, 1312, 146, 46))
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