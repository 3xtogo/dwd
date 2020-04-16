#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Autor: 3xtogo
    Status: Development
    Description: Main Application
"""

from helperFunctions import timeStamp, cTime
from displayData import DisplayData
from database.databaseDefinitions import *
from typing import List
import tkinter as tk
from PIL import Image, ImageTk


class PicturePath:
    home = r"assets/home.png"
    info = r"assets/info.png"
    infoBlue = r"assets/infoBlue.png"
    infoGreen = r"assets/infoGreen.png"
    infoRed = r"assets/infoRed.png"
    kalendar = r"assets/kalendar.png"


class Header(tk.Canvas):
    def __init__(self, master, **kw):
        tk.Canvas.__init__(self, master=master, **kw)
        self.master = master
        headerFontSmall = ("Helvetica", 16)
        headerFontBig = ("Helvetica", 36)
        self.clockStrVar = tk.StringVar()
        self.dateTimeLabel = tk.Label(master=master, textvariable=self.clockStrVar, font=headerFontSmall)
        self.dateTimeLabel.place(anchor=tk.NE, x=kw.get('width'), y=0)  # x=int(kw.get('width') / 2), y=int(kw.get('height') / 2))

        self.roomNameStrVar = tk.StringVar()
        self.roomNameLabel = tk.Label(master=master, textvariable=self.roomNameStrVar, font=headerFontBig)
        self.roomNameLabel.place(anchor=tk.NW, x=0, y=0)
        self.studienbereichStrVar = tk.StringVar()
        self.studienbereichLabel = tk.Label(master=master, textvariable=self.studienbereichStrVar, font=headerFontSmall)
        self.studienbereichLabel.place(anchor=tk.SE, x=kw.get('width'), y=kw.get('height'))

    def updateTime(self):
        self.clockStrVar.set(cTime())

    def setDynamicContent(self, d: DisplayData):
        self.roomNameStrVar.set(d.room.Gebaeude + '-' + d.room.Bezeichnung)
        self.studienbereichStrVar.set('Fachbereich: ' + d.room.Fachbereich + '\nStudienbereich: ' + d.room.Studienbereich)


class MyScreen(tk.Frame):

    def __init__(self, master, name, displayWidth, displayHeight, buttonHeight, buttonWidth, headerWidth, headerHeight, buttonIndex, picPath, **kw):
        tk.Frame.__init__(self, master=master, **kw)

        self._fontBig = ("Helvetica", 36)
        self._fontSmall = ("Helvetica", 16)

        self.name = name

        self.tkCanv_buttonCanvas = tk.Canvas(master=master, height=buttonHeight, width=buttonWidth,
                                             bg='white',
                                             # bg=kw.get('bg')
                                             )
        self.tkCanv_buttonCanvas.place(anchor=tk.NW, x=headerWidth, y=buttonIndex * buttonHeight)
        self.tkCanv_buttonCanvas.bind('<Button-1>', self.buttonPress)

        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight

        self.buttonPath = None
        self.buttonImage = None
        self.updateButtonPicture(picPath)

        self.tkCanv_leftscreen = tk.Canvas(master=self, height=displayHeight, width=int(displayWidth / 2), bg='white')
        self.tkCanv_rightscreen = tk.Canvas(master=self, height=displayHeight, width=int(displayWidth / 2), bg='white')

        self.tkCanv_leftscreen.place(anchor=tk.NW, x=0, y=0)
        self.tkCanv_rightscreen.place(anchor=tk.NW, x=int(displayWidth / 2), y=0)

        self.mainLable = tk.Label(master=self, font=self._fontBig)
        self.mainLable.place(x=0, y=0, anchor=tk.NW)

    def updateButtonPicture(self, picturePath):
        self.buttonPath = picturePath
        self.buttonImage = Image.open(picturePath)
        self.buttonImage = self.buttonImage.resize((100, 100), Image.ANTIALIAS)
        self.buttonImage = ImageTk.PhotoImage(self.buttonImage)
        self.tkCanv_buttonCanvas.create_image(self.buttonWidth / 2, self.buttonHeight / 2, anchor=tk.CENTER,
                                              image=self.buttonImage)

    def buttonPress(self, ev):
        self.tkraise()
        print(timeStamp(), "Button {} Pressed".format(self.name))


class HomeScreen(MyScreen):
    def __init__(self, master, name, **kw):
        MyScreen.__init__(self, master=master, name=name, **kw)
        self.mainLable.config(text="Home")

        self.dozenten: List[Dozent] = []
        self.buttons = []

    def optionButtonPressed(self, ev):
        for idx, button in enumerate(self.buttons):
            if button == ev.widget:
                print(ev, "was pressed", self.dozenten[idx].Nachname, 'will be printed')
                self.tkCanv_rightscreen.delete("all")
                doz = self.dozenten[idx]
                self.tkCanv_rightscreen.create_text(10, 0, font=self._fontSmall, anchor=tk.NW, text="{} {}\nE-Mail:\n{}\nTelefonnummer:\n{}\nStudip-Link:\n{}\nSprechzeiten:\n{}\n<Bild></Bild>".
                                                    format(doz.Vorname, doz.Nachname, doz.E_Mail, doz.Telefonnummer, doz.StudIP_Link, doz.Sprechzeiten))
        ...

    def showDefault(self):
        pass

    def loadData(self, displayData: DisplayData):
        self.dozenten = displayData.dozenten
        self.buttons = []
        maxInd = len(self.dozenten) - 1
        for dozent in self.dozenten:
            self.buttons.append(tk.Label(master=self, text=dozent.Nachname, font=self._fontSmall))
            self.buttons[-1].place(anchor=tk.NW, x=0, y=len(self.buttons) * int(110 / maxInd) + 20)  # todo spacing
        ...

        for button in self.buttons:
            button.bind('<Button-1>', self.optionButtonPressed)


class CalendarScreen(MyScreen):
    def __init__(self, master, name, **kw):
        MyScreen.__init__(self, master=master, name=name, **kw)
        self.mainLable.config(text="Kalender")

        self.kalenderEintraege: List[Kalender] = []
        self.buttons = []

    def optionButtonPressed(self, ev):
        for idx, button in enumerate(self.buttons):
            if button == ev.widget:
                print(ev, "was pressed Start:", self.kalenderEintraege[idx].StartUhrzeit, 'will be printed')
                self.tkCanv_rightscreen.delete("all")
                kal = self.kalenderEintraege[idx]
                self.tkCanv_rightscreen.create_text(10, 0, font=self._fontSmall, anchor=tk.NW, text="Kalenderereignis ID={}\nWochentag:{}\nStartuhrzeit: {}\nEnduhrzeit: {}\nEreignis: {}".
                                                    format(kal.ID, kal.WochentagTag, kal.StartUhrzeit, kal.Endurzeit, kal.Ereignis))
        ...

    def showDefault(self):
        pass

    def loadData(self, displayData: DisplayData):
        self.kalenderEintraege = displayData.kalenders
        self.buttons = []
        maxInd = len(self.kalenderEintraege) - 1
        for kalender in self.kalenderEintraege:
            self.buttons.append(tk.Label(master=self, text=kalender.Ereignis, font=self._fontSmall))
            self.buttons[-1].place(anchor=tk.NW, x=0, y=len(self.buttons) * int(110 / maxInd) + 20)  # todo spacing
        ...

        for button in self.buttons:
            button.bind('<Button-1>', self.optionButtonPressed)


class InfoScreen(MyScreen):
    def __init__(self, master, name, **kw):
        MyScreen.__init__(self, master=master, name=name, **kw)
        self.mainLable.config(text="Info")

        self.info: List[Information] = []
        self.buttons = []

    def optionButtonPressed(self, ev):
        for idx, button in enumerate(self.buttons):
            if button == ev.widget:
                print(ev, "was pressed", self.info[idx].InfoText, 'will be printed')
                self.tkCanv_rightscreen.delete("all")
                inf = self.info[idx]
                self.tkCanv_rightscreen.create_text(10, 0, font=self._fontSmall, anchor=tk.NW, text="inf.ID:{}\ninf.AnzeigeDauer:{}\ninf.DozID:{}\ninf.InfoText:\n".
                                                    format(inf.ID, inf.AnzeigeDauer, inf.DozID, inf.InfoText))
        ...

    def showDefault(self):
        pass

    def loadData(self, displayData: DisplayData):
        self.info = displayData.infos
        self.buttons = []
        maxInd = len(self.info) - 1
        for inf in self.info:
            self.buttons.append(tk.Label(master=self, text=inf.InfoText, font=self._fontSmall))
            self.buttons[-1].place(anchor=tk.NW, x=0, y=len(self.buttons) * int(110 / maxInd) + 20)  # todo spacing
        ...

        for button in self.buttons:
            button.bind('<Button-1>', self.optionButtonPressed)


class MainApplication:
    def __init__(self, **kwargs):
        self.displayId = kwargs.get('displayId')

        # some updateLocalDb
        self.displayData = DisplayData(self.displayId)
        # self.displayData.fetchFromLocalDb()

        # configs
        self.config_screenHeight = kwargs.get('screenHeight')
        self.config_screenWidth = kwargs.get('screenWidth')
        self.config_showBarOnTop = kwargs.get('showBarOnTop')
        self.config_showCursor = kwargs.get('showCursor')
        self.config_title = kwargs.get('title')
        self.config_showExitButton = kwargs.get('showExitButton')

        self.config_buttonWidthFactor = 0.2
        self.config_headerHeightFactor = 0.2
        self.config_numOfButtons = 3
        ## CALCULATION

        screenWidth = int(self.config_screenWidth)
        screenHeight = int(self.config_screenHeight)

        headerWidth = int(self.config_screenWidth * (1.0 - self.config_buttonWidthFactor))
        headerHeight = int(self.config_screenHeight * self.config_headerHeightFactor)

        buttonWidth = int(self.config_screenWidth * self.config_buttonWidthFactor)
        buttonHeight = int(self.config_screenHeight / self.config_numOfButtons)

        displayWidth = int(self.config_screenWidth * (1.0 - self.config_buttonWidthFactor))
        displayHeight = int(self.config_screenHeight * (1.0 - self.config_headerHeightFactor))

        ## WINDOW PROPERTIES
        self.root = tk.Tk()  # self.root: window

        # set window title
        self.root.title(self.config_title)

        # set geometry
        self.root.geometry('{}x{}'.format(
            self.config_screenWidth,
            self.config_screenHeight))

        # no bar on top # also fullscreen on the rasberry pi monitor
        if not self.config_showBarOnTop:
            self.root.overrideredirect(1)

        # no cursor visible on screen remove # for release on target hardware # REMOVE '#' LATER
        if not self.config_showCursor:
            self.root.config(cursor="none")

        ## WIDGETS
        self.header = Header(master=self.root, height=headerHeight, width=headerWidth, bg='white')
        self.header.place(x=0, y=0, anchor=tk.NW)

        # self.mainBackground = tk.Label(self.root, width=screenWidth, height=screenHeight, bg="black")
        # self.mainBackground.place(anchor=tk.NW, x=0, y=0)

        # self.buttonBackground = tk.Label(self.root, width=buttonWidth, height=screenHeight, bg="white")
        # self.buttonBackground.place(anchor=tk.NW, x=headerWidth, y=0)
        self.homeScreen = HomeScreen(master=self.root, height=displayHeight, width=displayWidth, buttonHeight=buttonHeight,
                                     buttonWidth=buttonWidth, buttonIndex=0, headerWidth=headerWidth, headerHeight=headerHeight, displayWidth=displayWidth, displayHeight=displayHeight,
                                     picPath=PicturePath.home, bg='red',
                                     name='Screen1')
        self.calendarScreen = CalendarScreen(master=self.root, height=displayHeight, width=displayWidth, buttonHeight=buttonHeight,
                                             buttonWidth=buttonWidth, buttonIndex=1, headerWidth=headerWidth, headerHeight=headerHeight, displayWidth=displayWidth, displayHeight=displayHeight,
                                             picPath=PicturePath.kalendar, bg='yellow',
                                             name='Screen2')
        self.infoScreen = InfoScreen(master=self.root, height=displayHeight, width=displayWidth, buttonHeight=buttonHeight,
                                     buttonWidth=buttonWidth, buttonIndex=2, headerWidth=headerWidth, headerHeight=headerHeight, displayWidth=displayWidth, displayHeight=displayWidth,
                                     picPath=PicturePath.info, bg='green',
                                     name='Screen3')

        self.homeScreen.place(anchor=tk.NW, x=0, y=headerHeight)
        self.calendarScreen.place(anchor=tk.NW, x=0, y=headerHeight)
        self.infoScreen.place(anchor=tk.NW, x=0, y=headerHeight)

        if self.config_showExitButton:
            EXITBUTTON = tk.Button(self.root,
                                   bg="grey",
                                   text="App beenden",
                                   command=self.buttenEndPress)
            EXITBUTTON.place(anchor=tk.NE, x=self.config_screenWidth, y=0)
            REFRESHBUTTON = tk.Button(bg="grey",
                                      text="Refresh",
                                      command=self.refreshRoutine)
            REFRESHBUTTON.place(anchor=tk.SE, x=self.config_screenWidth,
                                y=self.config_screenHeight)

        self.teststate = 'None'

        self.homeScreen.buttonPress(None)

    def updateDynamicContent(self):
        self.header.setDynamicContent(self.displayData)
        self.homeScreen.loadData(self.displayData)
        self.calendarScreen.loadData(self.displayData)
        self.infoScreen.loadData(self.displayData)

    def timeLoop(self):
        self.header.updateTime()
        # print(timeStamp(), 'updated time label')
        self.root.after(1000, self.timeLoop)

    def startApplication(self):
        # get dynamicContentFromDb and set content
        self.updateDynamicContent()

        # run clock loop
        self.timeLoop()
        self.root.mainloop()  # buttons active

    def refreshRoutine(self):
        self.updateDynamicContent()

        # this is just for test
        self.makeInfoBlue()

    def makeInfoBlue(self):
        if self.teststate == 'None':
            self.infoScreen.updateButtonPicture(PicturePath.infoRed)
            self.teststate = 'Red'
        else:
            self.infoScreen.updateButtonPicture(PicturePath.infoGreen)
            self.teststate = 'None'

    def buttenEndPress(self):
        self.root.destroy()


if __name__ == '__main__':
    # configuration for the main window

    wnd = MainApplication(
        showBarOnTop=True,
        showCursor=True,
        showExitButton=True,
        screenHeight=480,
        screenWidth=800,
        title='Demo',
        displayId=1
    )

    wnd.startApplication()

    # todo: anzeige screen1
    # todo: anzeige screen2
    # todo: anzeige screen3
    # todo: update displayData from local db when the database has new content
    # todo: server db ?
    # todo screen that can access the db and change entries (cmdline first)
