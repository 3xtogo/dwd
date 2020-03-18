import tkinter as tk
from helper.functions import timeStamp


class MainWindow:

    def __init__(self, **kwargs):
        self.config_screenHeight = kwargs.get('screenHeight')
        self.config_screenWidth = kwargs.get('screenWidth')
        self.config_showBarOnTop = kwargs.get('showBarOnTop')
        self.config_showCursor = kwargs.get('showCursor')
        self.config_title = kwargs.get('title')
        self.config_showExitButton = kwargs.get('showExitButton')

        # window properties
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

        # MainLayout
        buttonFactor = 0.2  # todo make config

        screenWidth = self.config_screenWidth * (1.0 - buttonFactor)
        sceenHeight = self.config_screenHeight
        self.screen = tk.Label(self.root, width=int(screenWidth), height=int(sceenHeight), bg="black")
        self.screen.place(x=0, y=0, anchor="nw", width=self.config_screenWidth, height=self.config_screenHeight)

        self.buttonArray = tk.Label(self.root, bg="white")
        self.buttonArray.place(x=int(self.config_screenWidth - self.config_screenWidth * buttonFactor), y=0,
                               anchor="nw",
                               width=int(self.config_screenWidth * buttonFactor), height=self.config_screenHeight)

        self.button1 = tk.Label(self.root, bg="white")
        self.button2 = tk.Label(self.root, bg="grey")
        self.button3 = tk.Label(self.root, bg="white")

        self.button1.place(anchor="nw", x=self.config_screenWidth - self.config_screenWidth * buttonFactor,
                           y=int(0 * sceenHeight / 3), width=int(self.config_screenWidth * buttonFactor),
                           height=int(sceenHeight / 3))
        self.button2.place(anchor="nw", x=self.config_screenWidth - self.config_screenWidth * buttonFactor,
                           y=int(1 * sceenHeight / 3), width=int(self.config_screenWidth * buttonFactor),
                           height=int(sceenHeight / 3))
        self.button3.place(anchor="nw", x=self.config_screenWidth - self.config_screenWidth * buttonFactor,
                           y=int(2 * sceenHeight / 3), width=int(self.config_screenWidth * buttonFactor),
                           height=int(sceenHeight / 3))

        # bind button klick funcs
        self.button1.bind("<Button-1>", self.button1Press)
        self.button2.bind("<Button-1>", self.button2Press)
        self.button3.bind("<Button-1>", self.button3Press)


        # heder
        self.header = tk.Label(self.root, bg="grey")
        self.header.place(x=0, y=0, height=self.config_screenHeight * 0.2,
                          width=int(self.config_screenWidth * (1.0 - buttonFactor)))

        # HSRM LOGO
        photoDir = r"assets/Logo_kompakt.png"
        image = tk.PhotoImage(file=photoDir)
        disp = image.subsample(10, 10)

        tk.Label(self.root,
                 image=disp,
                 bg="white").place()

        #     # Main window
        #     MainWindow.MainWindowText = tk.StringVar()  # This Variable is a placeholder
        #     label = tk.Label(self.root,textvariable=self.MainWindowText).grid(row=1,column=1)
        #     MainWindow.MainWindowText.set("Press a Button")

        if self.config_showExitButton:
            EXITBUTTON = tk.Button(self.root,
                                   bg="grey",
                                   text="App beenden",
                                   command=self.buttenEndPress).place(anchor=tk.NE, x=self.config_screenWidth, y=0)
            REFRESHBUTTON = tk.Button(bg="grey",
                                      text="Refresh").place(anchor=tk.SE, x=self.config_screenWidth,
                                                            y=self.config_screenHeight)
        #
        #     # run main
        self.root.mainloop()  # buttons active

    # # ButtonFuncs
    @staticmethod
    def button1Press(ev):
        # MainWindow.MainWindowText.set("Hello World")
        print(timeStamp(), "Button1 Pressed")

    @staticmethod
    def button2Press(ev):
        # MainWindow.MainWindowText.set("Hello World")
        print(timeStamp(), "Button2 Pressed")

    @staticmethod
    def button3Press(ev):
        # MainWindow.MainWindowText.set("Hello World")
        print(timeStamp(), "Button3 Pressed")

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
