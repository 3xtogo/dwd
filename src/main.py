import tkinter as tk
from src.helper.functions import timeStamp


class ButtonFrame:
    def __init__(self):
        self.frame = tk.Frame()
        self.frame


class MainWindow:

    def __init__(self, **kwargs):
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

        # MainLayout
        self.screen = tk.Frame(self.root).grid(row=0,
                                               column=0)
        self.buttonArray = tk.Frame(self.root).grid(row=0,
                                                    column=1)

        self.button1 = tk.Frame(self.root, width=200, height=self.config_screenHeight/3, bg="red").grid(row=0, column=2)
        self.button2 = tk.Frame(self.root, width=200, height=self.config_screenHeight/3, bg="yellow").grid(row=1, column=2)
        self.button3 = tk.Frame(self.root, width=200, height=self.config_screenHeight/3, bg="green").grid(row=2, column=2)

        self.root.mainloop()

    #     FrameN = tk.Frame(self.root,
    #                       width=self.config_screenWidth,
    #                       height=NorthHeight,
    #                       bg="white").grid(row=0,
    #                                        column=0,
    #                                        columnspan=3)
    #     FrameCenter = tk.Frame(self.root,
    #                            width=self.config_screenWidth,
    #                            height=CenterHeight,
    #                            bg="black").grid(row=1,
    #                                             column=0,
    #                                             columnspan=3)
    #     FrameSE = tk.Frame(self.root,
    #                        width=267,
    #                        height=100,
    #                        bg="red").grid(row=2,
    #                                       column=0)
    #     FrameS = tk.Frame(self.root,
    #                       width=266,
    #                       height=100,
    #                       bg="green").grid(row=2,
    #                                        column=1)
    #     FrameSW = tk.Frame(self.root,
    #                        width=267,
    #                        height=100,
    #                        bg="blue").grid(row=2,
    #                                        column=2)
    #
    #     # HSRM LOGO # ROW 0
    #     photoDir = r"assets/Logo_kompakt.png"
    #
    #     image = tk.PhotoImage(file=photoDir)
    #
    #     disp = image.subsample(10, 10)
    #
    #     tk.Label(FrameN,
    #              image=disp,
    #              bg="white").grid(columnspan=3,
    #                               row=0,
    #                               column=0)  # Top middle
    #
    #     # Main window
    #     MainWindow.MainWindowText = tk.StringVar()  # This Variable is a placeholder
    #     label = tk.Label(self.root,
    #                      textvariable=self.MainWindowText).grid(row=1,
    #                                                             column=1)
    #     MainWindow.MainWindowText.set("Press a Button")
    #
    #     # Buttondefinition
    #     ButtonRow = 2
    #     BUTTON1 = tk.Button(FrameSE,
    #                         bg="red",
    #                         text="hello",
    #                         command=MainWindow.Button1Press).grid(column=0,
    #                                                               row=ButtonRow)
    #
    #     BUTTON2 = tk.Button(FrameS,
    #                         bg="green",
    #                         text="wie gehts",
    #                         command=MainWindow.Button2Press).grid(column=1,
    #                                                               row=ButtonRow)
    #     BUTTON3 = tk.Button(FrameSW,
    #                         bg="blue",
    #                         text="dont Press This Button",
    #                         command=MainWindow.Button3Press).grid(column=2,
    #                                                               row=ButtonRow)
    #
    #     # Exitbutton
    #     EXITBUTTON = tk.Button(self.root,
    #                            bg="red",
    #                            text="App beenden",
    #                            command=self.buttenEndPress).place(x=0,
    #                                                               y=0)  # REMOVE LATER
    #
    #     # run main
    #     self.root.mainloop()  # buttons active
    #
    # # Buttons
    # # ButtonFuncs
    # @staticmethod
    # def Button1Press():
    #     MainWindow.MainWindowText.set("Hello World")
    #     print(timeStamp(), "Hello World")
    #
    # @staticmethod
    # def Button2Press():
    #     MainWindow.MainWindowText.set("HELLO WORLD")
    #     print(timeStamp(), "HELLO WORLD")
    #
    # @staticmethod
    # def Button3Press():
    #     MainWindow.MainWindowText.set("h3110 w0r1D")
    #     print(timeStamp(), "h3110 w0r1D")
    #
    # def buttenEndPress(self):
    #     self.root.destroy()


if __name__ == '__main__':
    # setupLocalDatabase()
    print("x")
    # configuration for the main window
    wnd = MainWindow(
        showBarOnTop=True,
        showCursor=True,
        screenHeight=480,
        screenWidth=800,
        title='Demo'
    )
