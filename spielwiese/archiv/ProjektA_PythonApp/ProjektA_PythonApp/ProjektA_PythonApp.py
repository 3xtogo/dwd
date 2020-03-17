import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime

def makeJson(filename):
        #make a dictionary
        # {<key>:<value>} dict
        # [<listelem0>,<listelem1>,...] list
        # (<elem1>,<elem2>) tuple
        mydict = {'roomNumber':'<RoomId>',
                  'TimeTable':[('10:00-13:15','PPP-Tutorium'),
                          ('13:30-15:00','PPP-Tutorium')]}
        
        #make a jsonfile from mydict
        with open(filename,'w') as f:
                json.dump(mydict,f)
                
def getDict(filename):
        with open(filename) as f: #open the file
                str = f.read() #read the file into a string
                DATA = json.loads(str) #make a dict out of the string
                #print(type(jstr))

        return DATA

root = tk.Tk() #root: window main frame instance
root.title("layout2")
#screensize
ScreenHeight = 480
ScreenWidth = 800
root.geometry('{}x{}'.format(ScreenWidth,ScreenHeight))

root.overrideredirect(1) # no bar on top 
root.config(cursor="none") #no cursor visible

#Framelayout
#Frames:rootLeft                                        OK
#               |---Header                                      OK
#               |       |---Logo                                OK
#               |       |---Headlabel                   OK
#               |       |---Time                                OK
#               |               |---ClockLabel          OK - TODO: size, font, bg ...?
#               |
#               |---Body                                        OK
#               |       |---BodyLeft                    OK
#               |       |       |---RoomNr
#               |       |       |---textboxSmall
#               |       |
#               |       |---BodyRight                   OK
#               |               |---textboxBig
#               |
#               rootRight                               OK
#               |---buttonFrame1                OK
#               |---buttonFrame2                OK      
#               |---buttonFrame3                OK

Buttoncount = 3
Buttonshrinkfactor = 0.6
ButtonWidth = (ScreenHeight/Buttoncount) * Buttonshrinkfactor
LeftWidht = ScreenWidth - ButtonWidth
RightWidth = ScreenWidth -LeftWidht

#rootLeft 
rootLeft = tk.Frame(root,width = LeftWidht,height = ScreenHeight)
rootLeft.grid(column = 0,row = 0)

#Header
HEADERHEIGHT = ScreenHeight* 0.15

Header = tk.Frame(rootLeft, width = LeftWidht, height  = HEADERHEIGHT, bg = "yellow")
Header.grid(column = 0, row = 0)

headlabelwidht = LeftWidht * 0.5
logowidth = (LeftWidht-headlabelwidht)/2
timewidth = LeftWidht-headlabelwidht-logowidth

#Logo
Logo = tk.Frame(Header,height = HEADERHEIGHT, width = logowidth,bg = "grey")
Logo.grid(column = 0, row = 0)

#Headlabel
Headlabel = tk.Frame(Header, height = HEADERHEIGHT, width = headlabelwidht, bg = "white")
Headlabel.grid(column = 1, row = 0)

#Time
Time = tk.Frame(Header,  height = HEADERHEIGHT, width = timewidth, bg = "black")
Time.grid(column = 2, row = 0)

#getTimeStrfunc
def getTimeStr():
        return datetime.now().strftime("%H:%M:%S")

dspTime = tk.StringVar()
dspTime.set(getTimeStr())
Clock = tk.Label(Time,textvariable = dspTime)
Clock.place(relx=.5,rely=.5,anchor="center")

#Body 
Body = tk.Frame(rootLeft, width = LeftWidht, height  = ScreenHeight-HEADERHEIGHT, bg = "orange")
Body.grid(column = 0, row = 1)

BodypartWidht = LeftWidht * 0.5

#BodyLeft
BodyLeft = tk.Frame(Body, width = BodypartWidht, height = ScreenHeight-HEADERHEIGHT, bg = "red")
BodyLeft.grid(column=0,row = 0)

#BodyRight
BodyRight = tk.Frame(Body, width = BodypartWidht, height = ScreenHeight-HEADERHEIGHT, bg = "green")
BodyRight.grid(column=1,row = 0)

#rootRight
rootRight = tk.Frame(root, width = RightWidth,height = ScreenHeight)
rootRight.grid(column = 1,row = 0)

#ButtonFrames
buttonFrame1 = tk.Frame(rootRight,width = RightWidth,height = ScreenHeight/3, bg = "lightblue")
buttonFrame1.grid(column = 0, row = 0)

buttonFrame2 = tk.Frame(rootRight,width = RightWidth,height = ScreenHeight/3, bg = "blue")
buttonFrame2.grid(column = 0, row = 1)

buttonFrame3 = tk.Frame(rootRight,width = RightWidth,height = ScreenHeight/3, bg = "navy")
buttonFrame3.grid(column = 0, row = 2)

#TimeUpdatefunc
def TimeUpdate():
        global dspTime
        now = getTimeStr()
        if now != dspTime.get():
                dspTime.set(now) #changes the Time
                #print(dspTime.get())
                #print("Time Updated to "+ dspTime.get())
                root.after(1000,TimeUpdate)
        else:
                root.after(1000,TimeUpdate)

#functions on event Buttonklick
def button1(event):
        print("button1Press")
        BodyRight.configure(bg="lightblue")     #lightblue
        
def button2(event):
        print("button2Press")
        BodyRight.configure(bg="blue")  #blue
        
def button3(event):
        print("button3Press")   #navy
        BodyRight.configure(bg="navy")

#buttonfuncs
buttonFrame1.bind("<Button-1>",button1)
buttonFrame2.bind("<Button-1>",button2)
buttonFrame3.bind("<Button-1>",button3)


print("JETZT")

#main
if __name__ == "__main__":
        filename = 'content.json'
        makeJson(filename)

        mydict = getDict(filename)
        print(mydict)
        print("hello World")
        root.after(1000,TimeUpdate)
        root.mainloop()
