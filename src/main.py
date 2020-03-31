from helper.functions import timeStamp
from database.localDb.localDb import LocalDb

import tkinter as tk
from PIL import Image, ImageTk


# from createDatabase import mainCreateDatabase


class PicturePath:
    home = r"assets/home.png"
    info = r"assets/info.png"
    infoBlue = r"assets/infoBlue.png"
    infoGreen = r"assets/infoGreen.png"
    infoRed = r"assets/infoRed.png"
    kalendar = r"assets/kalendar.png"


class MyScreen(tk.Frame):

    def __init__(self, master, name, buttonHeight, buttonWidth, headerWidth, buttonIndex, picPath, **kw):
        tk.Frame.__init__(self, master=master, **kw)

        self.name = name
        ###
        #
        self.buttonCanvas = tk.Canvas(master=master, height=buttonHeight, width=buttonWidth,
                                      bg='white',
                                      # bg=kw.get('bg')
                                      )
        self.buttonCanvas.place(anchor=tk.NW, x=headerWidth, y=buttonIndex * buttonHeight)
        self.buttonCanvas.bind('<Button-1>', self.buttonPress)

        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight

        self.buttonPath = None
        self.buttonImage = None
        self.updateButtonPicture(picPath)

    def updateButtonPicture(self, picturePath):
        self.buttonPath = picturePath
        self.buttonImage = Image.open(picturePath)
        self.buttonImage = self.buttonImage.resize((100, 100), Image.ANTIALIAS)
        self.buttonImage = ImageTk.PhotoImage(self.buttonImage)
        self.buttonCanvas.create_image(self.buttonWidth / 2, self.buttonHeight / 2, anchor=tk.CENTER, image=self.buttonImage)

    def buttonPress(self, ev):
        self.tkraise()
        print(timeStamp(), "Button {} Pressed".format(self.name))


class Header(tk.Frame):
    def __init__(self, master, **kw):
        tk.Frame.__init__(self, master=master, **kw)
        print(tk.Frame.winfo_width(self))
        print(tk.Frame.winfo_height(self))


class MySpecialScreen(MyScreen):

    def __init__(self, master, name, **kw):
        MyScreen.__init__(self, master=master, name=name, **kw)


class MainApplication:
    def __init__(self, **kwargs):
        """Main Application runs on Device"""
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
        # self.mainBackground = tk.Label(self.root, width=screenWidth, height=screenHeight, bg="black")
        # self.mainBackground.place(anchor=tk.NW, x=0, y=0)

        # self.buttonBackground = tk.Label(self.root, width=buttonWidth, height=screenHeight, bg="white")
        # self.buttonBackground.place(anchor=tk.NW, x=headerWidth, y=0)
        self.screen1 = MyScreen(master=self.root, height=displayHeight, width=displayWidth, buttonHeight=buttonHeight, buttonWidth=buttonWidth, buttonIndex=0, headerWidth=headerWidth, picPath=PicturePath.home, bg='red',
                                name='Screen1')
        self.screen2 = MyScreen(master=self.root, height=displayHeight, width=displayWidth, buttonHeight=buttonHeight, buttonWidth=buttonWidth, buttonIndex=1, headerWidth=headerWidth, picPath=PicturePath.kalendar, bg='yellow',
                                name='Screen2')
        self.screen3 = MyScreen(master=self.root, height=displayHeight, width=displayWidth, buttonHeight=buttonHeight, buttonWidth=buttonWidth, buttonIndex=2, headerWidth=headerWidth, picPath=PicturePath.info, bg='green',
                                name='Screen3')

        self.screen1.place(anchor=tk.NW, x=0, y=headerHeight)
        self.screen2.place(anchor=tk.NW, x=0, y=headerHeight)
        self.screen3.place(anchor=tk.NW, x=0, y=headerHeight)

        if self.config_showExitButton:
            EXITBUTTON = tk.Button(self.root,
                                   bg="grey",
                                   text="App beenden",
                                   command=self.buttenEndPress).place(anchor=tk.NE, x=self.config_screenWidth, y=0)
            REFRESHBUTTON = tk.Button(bg="grey",
                                      text="Refresh",
                                      command=self.refreshRoutine).place(anchor=tk.SE, x=self.config_screenWidth,
                                                                         y=self.config_screenHeight)

        self.teststate = 'None'

        # run main
        self.root.mainloop()  # buttons active

    def refreshRoutine(self):

        self.makeInfoBlue()

    def makeInfoBlue(self):
        if self.teststate == 'None':
            self.screen3.updateButtonPicture(PicturePath.infoRed)
            self.teststate = 'Red'
        else:
            self.screen3.updateButtonPicture(PicturePath.infoGreen)
            self.teststate = 'None'

    def buttenEndPress(self):
        self.root.destroy()


if __name__ == '__main__':
    # configuration for the main window

    LocalDb()


    wnd = MainApplication(
        showBarOnTop=True,
        showCursor=True,
        showExitButton=True,
        screenHeight=480,
        screenWidth=800,
        title='Demo'
    )

    # todo: Beispieldaten anlegen

    # todo: joined Table anlegen

    # todo: a clock with tk.Stringvar in a canvas and self.root.after(1000, self.TimeUpdate())

    # todo: anzeige screen1

    # todo: anzeige screen2

    # todo: anzeige screen3

    # todo: fetch Data For Screen From local Database

    # todo: update mechanism for screen from local db

    # todo: server db

    # todo screen that can access the db and change entries (optional)

