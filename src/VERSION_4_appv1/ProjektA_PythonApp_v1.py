import tkinter as tk
import json
from datetime import datetime

#Framelayout
#Frames:
#root:
#		rootLeft					OK
#		|---Header					OK
#		|	|---Logo<-Frame			OK
#		|	|---headBanner			OK
#		|	|---Time				OK
#		|		|---ClockLabel		OK - TODO: size, font, bg ...?
#		|
#		|---Body					OK
#		|	|---BodyLeft			OK
#		|	|	|---RoomNr
#		|	|	|---textboxSmall
#		|	|
#		|	|---BodyRight			OK
#		|		|---textboxBig
#		|
#		rootRight				OK
#		|---buttonFrame1		OK
#		|---buttonFrame2		OK	
#		|---buttonFrame3		OK

font_Default=("Arial", 30)
font_BIG = ("Arial", 40)

class js():
        
	def makeJson(filename):
		#make a dictionary
		mydict = {'roomNumber':'<Raum 118>'}

		#make a jsonfile out of the dict
		with open(filename,'w') as f:
			json.dump(mydict,f)

	def getDict(filename):
		with open(filename) as f: #open the file
			str = f.read() #read the file into a string
			DATA = json.loads(str) #make a dict out of the string
			#print(type(jstr))
	
		return DATA
	
class app:
	def __init__(self, is_targetDevice):
		#isTargetDevice? bool 
		self.root = tk.Tk() #root: window main frame instance
		self.root.title("OOP DEMO")

		#screensize
		ScreenHeight = 480
		ScreenWidth = 800
		self.root.geometry('{}x{}'.format(ScreenWidth,ScreenHeight))

		if is_targetDevice:
			self.root.overrideredirect(1) # no bar on top 
			self.root.config(cursor="none") #no cursor visible
		
		Buttoncount = 3
		Buttonshrinkfactor = 0.6
		ButtonWidth = (ScreenHeight/Buttoncount) * Buttonshrinkfactor
		LeftWidht = ScreenWidth - ButtonWidth
		RightWidth = ScreenWidth -LeftWidht

		#rootLeft 
		self.rootLeft = tk.Frame(self.root,width = LeftWidht,height = ScreenHeight)
		self.rootLeft.grid(column = 0,row = 0)

		#Header
		HEADERHEIGHT = ScreenHeight* 0.15

		self.Header = tk.Frame(self.rootLeft, width = LeftWidht, height  = HEADERHEIGHT, bg = "yellow")
		self.Header.grid(column = 0, row = 0)

		headBanner = LeftWidht * 0.5
		logowidth = (LeftWidht-headBanner)/2
		timewidth = LeftWidht-headBanner-logowidth

		#Logo
		self.Logo = tk.Frame(self.Header,height = HEADERHEIGHT, width = logowidth,bg = "blue")
		self.Logo.grid(column = 0, row = 0)
		
		raw = tk.PhotoImage(file = "hsrm.png")
		LogoImage = raw.subsample(5,5)
		self.LogoLabel = tk.Label(self.Logo,image = LogoImage)
		self.LogoLabel.place(relx=1,rely=1,anchor="center")
		#HIER FUNKTIONIERT gar nichts		

		#headBanner
		self.headBanner = tk.Frame(self.Header, height = HEADERHEIGHT, width = headBanner, bg = "white")
		self.headBanner.grid(column = 1, row = 0)

		#Time
		self.Time = tk.Frame(self.Header,  height = HEADERHEIGHT, width = timewidth, bg = "black")
		self.Time.grid(column = 2, row = 0)

		self.dspTime = tk.StringVar() 
		self.dspTime.set(app.getTimeStr())

		#Clock
		self.Clock = tk.Label(self.Time,textvariable = self.dspTime,font=font_Default)
		self.Clock.place(relx=.5,rely=.5,anchor="center")# temporäres layout

		#Body 
		self.Body = tk.Frame(self.rootLeft, width = LeftWidht, height  = ScreenHeight-HEADERHEIGHT, bg = "orange")
		self.Body.grid(column = 0, row = 1)

		BodypartWidht = LeftWidht * 0.5

		#BodyLeft
		self.BodyLeft = tk.Frame(self.Body, width = BodypartWidht, height = ScreenHeight-HEADERHEIGHT, bg = "red")
		self.BodyLeft.grid(column=0,row = 0)

		self.dspRoom = tk.StringVar()
		self.roomLabel = tk.Label(self.BodyLeft,textvariable = self.dspRoom,font = font_BIG)
		self.roomLabel.place(relx = 0.5,rely = 0.5,anchor = "center")

		#BodyRight
		self.BodyRight = tk.Frame(self.Body, width = BodypartWidht, height = ScreenHeight-HEADERHEIGHT, bg = "green")
		self.BodyRight.grid(column=1,row = 0)

		#rootRight
		self.rootRight = tk.Frame(self.root, width = RightWidth,height = ScreenHeight)
		self.rootRight.grid(column = 1,row = 0)

		#ButtonFrames
		self.buttonFrame1 = tk.Frame(self.rootRight,width = RightWidth,height = ScreenHeight/3, bg = "lightblue")
		self.buttonFrame1.grid(column = 0, row = 0)

		self.buttonFrame2 = tk.Frame(self.rootRight,width = RightWidth,height = ScreenHeight/3, bg = "blue")
		self.buttonFrame2.grid(column = 0, row = 1)

		self.buttonFrame3 = tk.Frame(self.rootRight,width = RightWidth,height = ScreenHeight/3, bg = "navy")
		self.buttonFrame3.grid(column = 0, row = 2)

		#buttonfuncs
		self.buttonFrame1.bind("<Button-1>",button1)
		self.buttonFrame2.bind("<Button-1>",button2)
		self.buttonFrame3.bind("<Button-1>",button3)

	def loadText(self,filename):
		mydict = js.getDict(filename)
		
		#set all textvariables
		self.dspRoom.set(mydict['roomNumber']) 
		
		print(mydict['roomNumber'])
		

	def loadContent(self):
		#get the dict

		contentdict = js.getDict('content.json')

		#make a dict out of the jsonstring
		#use the dict to set all label contents
		pass
	
	def getTimeStr():
		return datetime.now().strftime("%H:%M:%S")

	#TimeUpdatefunc
	def TimeUpdate(self):
		now = app.getTimeStr()
		if now != self.dspTime.get():
			#time changed
			self.dspTime.set(now) #change the Time variable
			#print(dspTime.get())
			#print("Time Updated to "+ dspTime.get())
			self.root.after(1000,self.TimeUpdate)
			return True
		else:
			#time did not change
			self.root.after(100,self.TimeUpdate)
			return False

	def startLoop(self): #!!! SPAGETTHI ALARM
		self.root.after(1000,self.TimeUpdate())
		print('hello-from startloop')
		self.root.mainloop()
		print('hello-from after mainloop ')


def button1(event):
	screen.BodyRight.config(bg="lightblue")
def button2(event):
	screen.BodyRight.config(bg="blue")
def button3(event):
	screen.BodyRight.config(bg="navy")
#----------------- application starts here ----------------- #

if __name__ == "__main__":

	screen = app(False) # main instance class # True for target hardware
	filename = 'content.json'
	screen.loadText(filename)

	js.makeJson(filename) # onlytemporary

	screen.loadContent()
	
	
	screen.startLoop()
