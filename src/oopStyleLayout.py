import tkinter as tk
from src.helper.functions import timeStamp
#from src.database.db import Db

#db = Db()


class Window:
    MainWindowText = None

    def __init__(self, **kwargs):
        # todo: make a ini file for that
        self.config_screenHeight = kwargs.get('screenHeight')
        self.config_screenWidth = kwargs.get('screenWidth')
        self.config_showBarOnTop = kwargs.get('showBarOnTop')
        self.config_showCursor = kwargs.get('showCursor')
        self.config_title = kwargs.get('title')

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

        # Frames for Layout
        NorthHeight = 100
        CenterHeight = 380 - NorthHeight
        FrameN = tk.Frame(self.root,
                          width=self.config_screenWidth,
                          height=NorthHeight,
                          bg="white").grid(row=0,
                                           column=0,
                                           columnspan=3)
        FrameCenter = tk.Frame(self.root,
                               width=self.config_screenWidth,
                               height=CenterHeight,
                               bg="black").grid(row=1,
                                                column=0,
                                                columnspan=3)
        FrameSE = tk.Frame(self.root,
                           width=267,
                           height=100,
                           bg="red").grid(row=2,
                                          column=0)
        FrameS = tk.Frame(self.root,
                          width=266,
                          height=100,
                          bg="green").grid(row=2,
                                           column=1)
        FrameSW = tk.Frame(self.root,
                           width=267,
                           height=100,
                           bg="blue").grid(row=2,
                                           column=2)

        # HSRM LOGO # ROW 0
        photoDir = r"assets/Logo_kompakt.png"

        image = tk.PhotoImage(file=photoDir)

        disp = image.subsample(10, 10)

        tk.Label(FrameN,
                 image=disp,
                 bg="white").grid(columnspan=3,
                                  row=0,
                                  column=0)  # Top middle

        # Main window
        Window.MainWindowText = tk.StringVar()  # This Variable is a placeholder
        label = tk.Label(self.root,
                         textvariable=self.MainWindowText).grid(row=1,
                                                                column=1)
        Window.MainWindowText.set("Press a Button")

        # Buttondefinition
        ButtonRow = 2
        BUTTON1 = tk.Button(FrameSE,
                            bg="red",
                            text="hello",
                            command=Window.Button1Press).grid(column=0,
                                                              row=ButtonRow)

        BUTTON2 = tk.Button(FrameS,
                            bg="green",
                            text="wie gehts",
                            command=Window.Button2Press).grid(column=1,
                                                              row=ButtonRow)
        BUTTON3 = tk.Button(FrameSW,
                            bg="blue",
                            text="dont Press This Button",
                            command=Window.Button3Press).grid(column=2,
                                                              row=ButtonRow)

        # Exitbutton
        EXITBUTTON = tk.Button(self.root,
                               bg="red",
                               text="App beenden",
                               command=self.buttenEndPress).place(x=0,
                                                                y=0)  # REMOVE LATER

        # run main
        self.root.mainloop()  # buttons active

    # Buttons
    # ButtonFuncs
    @staticmethod
    def Button1Press():
        Window.MainWindowText.set("Hello World")
        print(timeStamp(), "Hello World")

    @staticmethod
    def Button2Press():
        Window.MainWindowText.set("HELLO WORLD")
        print(timeStamp(), "HELLO WORLD")

    @staticmethod
    def Button3Press():
        Window.MainWindowText.set("h3110 w0r1D")
        print(timeStamp(), "h3110 w0r1D")



    def buttenEndPress(self):
        self.root.destroy()

if __name__ == '__main__':
    # configuration for the main window
    wnd = Window(
        showBarOnTop=True,
        showCursor=True,
        screenHeight=480,
        screenWidth=800,
        title='Demo'
    )
