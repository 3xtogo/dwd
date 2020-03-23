import tkinter as tk
from helper.functions import timeStamp


class BaseScreen(tk.Frame):

    def __init__(self, master, name, **kw):
        tk.Frame.__init__(self, master=master, **kw)

        self.button = None
        self.buttonImage = None
        self.name = name

    def buttonPress(self, ev):
        self.tkraise()
        print(timeStamp(), "Button {} Pressed".format(self.name))


class SpecialBaseScreen(BaseScreen):

    def __init__(self, master, name, **kw):
        BaseScreen.__init__(self, master=master, name=name, **kw)


class MainWindow:

    def __init__(self, **kwargs):
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

        self.screen1 = BaseScreen(master=self.root, height=displayHeight, width=displayWidth, bg='red', name='Screen1')
        self.screen2 = BaseScreen(master=self.root, height=displayHeight, width=displayWidth, bg='yellow', name='Screen2')
        self.screen3 = SpecialBaseScreen(master=self.root, height=displayHeight, width=displayWidth, bg='green', name='Screen3')

        self.screen1.place(anchor=tk.NW, x=0, y=headerHeight)
        self.screen2.place(anchor=tk.NW, x=0, y=headerHeight)
        self.screen3.place(anchor=tk.NW, x=0, y=headerHeight)

        self.screen1.button = tk.Frame(master=self.root, height=buttonHeight, width=buttonWidth, bg='red')
        self.screen2.button = tk.Frame(master=self.root, height=buttonHeight, width=buttonWidth, bg='yellow')
        self.screen3.button = tk.Frame(master=self.root, height=buttonHeight, width=buttonWidth, bg='green')

        self.screen1.button.place(anchor=tk.NW, x=headerWidth, y=0 * buttonHeight)
        self.screen2.button.place(anchor=tk.NW, x=headerWidth, y=1 * buttonHeight)
        self.screen3.button.place(anchor=tk.NW, x=headerWidth, y=2 * buttonHeight)

        self.screen1.button.bind('<Button-1>', self.screen1.buttonPress)
        self.screen2.button.bind('<Button-1>', self.screen2.buttonPress)
        self.screen3.button.bind('<Button-1>', self.screen3.buttonPress)

        # # HSRM LOGO
        # photoDir = r"assets/Logo_kompakt.png"
        # image = tk.PhotoImage(file=photoDir)
        # disp = image.subsample(10, 10)
        #
        # tk.Label(self.root,
        #          image=disp,
        #          bg="white").place()
        #
        # #     # Main window
        # #     MainWindow.MainWindowText = tk.StringVar()  # This Variable is a placeholder
        # #     label = tk.Label(self.root,textvariable=self.MainWindowText).grid(row=1,column=1)
        # #     MainWindow.MainWindowText.set("Press a Button")

        if self.config_showExitButton:
            EXITBUTTON = tk.Button(self.root,
                                   bg="grey",
                                   text="App beenden",
                                   command=self.buttenEndPress).place(anchor=tk.NE, x=self.config_screenWidth, y=0)
            REFRESHBUTTON = tk.Button(bg="grey",
                                      text="Refresh").place(anchor=tk.SE, x=self.config_screenWidth,
                                                            y=self.config_screenHeight)

        # run main
        self.root.mainloop()  # buttons active

    def buttenEndPress(self):
        self.root.destroy()


if __name__ == '__main__':
    # setupLocalDatabase()
    # configuration for the main window
    wnd = MainWindow(
        showBarOnTop=True,
        showCursor=True,
        showExitButton=True,
        screenHeight=480,
        screenWidth=800,
        title='Demo'
    )
