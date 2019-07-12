import wx

# This will be ran separately from the main script and will generate the input file. This could be done through networks
# but that seems to be superfluous at this stage as well as having to rewrite sections of code in the main script.

class Window(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1000, 200))
        panel = wx.Panel(self)

        FileNameBox = wx.TextEntryDialog(None, "Please enter the name of the file you want to create. INCLUDE THE FILE EXTENSION!", "File Creator", "")
        if FileNameBox.ShowModal()==wx.ID_OK:
            fileName = FileNameBox.GetValue()

        PlayerListBox = wx.TextEntryDialog(None, "Please enter the full ordered list of players (including their battletags) according to the input guide", "Players", "")
        if PlayerListBox.ShowModal() == wx.ID_OK:
            playerList = PlayerListBox.GetValue()

        PlayerVoteBox = wx.TextEntryDialog(None, "Please enter all of the player votes according to the input guide (use / to signify a new line)", "Player Votes", "")
        if PlayerVoteBox.ShowModal() == wx.ID_OK:
            playerVoteString = PlayerVoteBox.GetValue()

        playerVote = self.stringToList(playerVoteString)

        self.writeToFile(fileName, playerList, playerVote)


    def stringToList(self, string):
        output = []

        tempString = ""
        for char in string:
            if char != '/':
                tempString = tempString + char
            else:
                output.append(tempString + '\n')
                tempString = ""

        return output

    def writeToFile(self, filename, playername, playervotes):
        file = open(filename, "w")
        file.write(playername)
        file.write('\n')
        file.writelines(playervotes)
        file.close()



app = wx.App(False)
frame = Window(None, 'Blink BOT Control')
app.MainLoop()