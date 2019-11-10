import tkinter as tk
  
root = tk.Tk() #root: window main frame instance
root.title("layout2")
#screensize
ScreenHeight = 480
ScreenWidth = 800
root.geometry('{}x{}'.format(ScreenWidth,ScreenHeight))

#root.overrideredirect(1) # no bar on top 
#root.config(cursor="none") #no cursor visible

rootLeft = tk.Frame(root)
rootLeft.grid(column = 0)
rootRight = tk.Frame(root)
rootRight.grid(column = 1, colour ="black")
    
#run main
root.mainloop()


#Frames for Layout 
NorthHeight = 100
CenterHeight = 380-NorthHeight
FrameN = tk.Frame(root,width = ScreenWidth,height = NorthHeight,bg = "white").grid(row=0,column=0,columnspan = 3)
FrameCenter = tk.Frame(root,width = ScreenWidth,height = CenterHeight,bg = "black").grid(row=1,column=0,columnspan = 3)
FrameSE = tk.Frame(root,width = 267, height = 100, bg = "red").grid(row = 2,column = 0)
FrameS = tk.Frame(root,width = 266, height = 100, bg = "green").grid(row = 2,column = 1)
FrameSW = tk.Frame(root,width = 267, height = 100, bg = "blue").grid(row = 2,column = 2)

#HSRM LOGO # ROW 0
image = tk.PhotoImage(file="Logo_kompakt.png")
disp = image.subsample(10,10)
tk.Label(FrameN,image=disp,bg="white").grid(columnspan = 3, row = 0, column = 0) #Top middle

#Main window
MainWindowText = tk.StringVar() #This Variable is a placeholder
label = tk.Label(root,textvariable=MainWindowText).grid(row = 1,column = 1)
MainWindowText.set("Press a Button")

#Buttons
#ButtonFuncs
def Button1Press():
    MainWindowText.set("Hello World")
    print("Hello World")
    
def Button2Press():
    MainWindowText.set("HELLO WORLD")
    print("HELLO WORLD")

def Button3Press():
    MainWindowText.set("h3110 w0r1D")
    print("h3110 w0r1D")

#Buttondefinition
ButtonRow = 2
BUTTON1 = tk.Button(FrameSE,bg = "red",text="hello",command = Button1Press).grid(column = 0, row = ButtonRow)
BUTTON2 = tk.Button(FrameS,bg = "green",text="wie gehts",command = Button2Press).grid(column = 1, row = ButtonRow)
BUTTON3 = tk.Button(FrameSW,bg = "blue",text="dont Press This Button",command = Button3Press).grid(column = 2, row = ButtonRow)

#Exitbutton
EXITBUTTON = tk.Button(root,bg = "red",text = "App beenden",command=root.destroy).place(x = 0, y = 0) # REMOVE LATER

