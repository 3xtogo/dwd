import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime

import socket #reference: https://realpython.com/python-sockets/
import threading

## json
def makeJson(filename):
        #make a dictionary
        # {<key>:<value>} dict
        # [<listelem0>,<listelem1>,...] list
        # (<elem1>,<elem2>) tuple
        mydict = {'key1':'value1'}
        
        #make a jsonfile from mydict
        with open(filename,'w') as f:
                json.dump(mydict,f)
                
def getDict(filename):
        with open(filename) as f: 
                str = f.read() 
                data = json.loads(str) #make a dict from string
                #print(type(jstr))

        return data

# server
def server(ip_addr,port,textvar):
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(ip_addr,port)
    serversocket.listen(5)

    while 1:
        (clientsocket, address) = serversocket.accept()
        data = clientsocket.recv(1024).decode()

# click Events

def clickFrame(event):
    event.widget.focus_set()
    print("clicked at", event.x, event.y)
    f1.create_arc(event.x,event.y,event.x+1,event.y+1)


def quit(event):
    print("EXIT")
    root.destroy()

# makeFramesCanvs...
        
def makeCanv(root):
        f1 = tk.Canvas(master = root, bg='grey',width = 500,height =  500)
        
        offs = 200
        y1 = 0
        y2 = y1+offs
        y3 = y2+offs

        f1.image1 = tk.PhotoImage(file='profile.gif')
        f1.create_image(0,y1,image=f1.image1,anchor = tk.NW)
        f1.image2 = tk.PhotoImage(file='profile.gif')
        f1.create_image(0,y2,image=f1.image1,anchor = tk.NW)
        f1.image3 = tk.PhotoImage(file='profile.gif')
        f1.create_image(0,y3,image=f1.image1,anchor = tk.NW)
        return f1

def makeOscar(root):

        f2 = tk.Canvas(master = root, bg='grey',width = 500,height =  500)
        
        f2.image1 = tk.PhotoImage(file='azm.gif')
        f2.create_image(0,0,image=f2.image1,anchor = tk.NW)
        return f2

myFont1 = ('Arial',50)
myFont2 = ('Arial',20)

# tkwindow
global root
root = tk.Tk() #root: window main frame instance
root.overrideredirect(1) # no bar on top 
#root.config(cursor='none')
ScreenHeight = 480
ScreenWidth = 800
root.geometry('{}x{}'.format(ScreenWidth,ScreenHeight))

#header
header = tk.Frame(master = root,bg = 'green',width = ScreenWidth,height = ScreenHeight*0.2);#height = 100,width = 800
#hCanv // hsrmLogo // funktioniert nicht als funktion vielleicht aber als Klasse
x_hsrm_logo = 95
y_hsrm_logo = 95
#headercanvas
hCanv = tk.Canvas(master=header,bg = 'white',height =y_hsrm_logo , width = x_hsrm_logo)
photoImage_hsrm = tk.PhotoImage(file = 'hsrm_logo.gif')
hCanv.create_image(x_hsrm_logo/2,y_hsrm_logo/2,image=photoImage_hsrm,anchor = tk.CENTER)
hCanv.pack(side = tk.LEFT)
#headerfeld 1

hLabel1 = tk.Label(master=header,bg='white',text ='A127',font=myFont1)
hLabel1.pack(side=tk.LEFT)

hLabel2 = tk.Label(master=header,bg='white',text ='Fachbereich ING',font=myFont2)
hLabel2.pack(side=tk.LEFT)

hLabel3 = tk.Label(master=header,bg='white',text ='<12:45>',font=myFont2)
hLabel3.pack(side=tk.RIGHT)





#TEMPLABEL = tk.Label(master=header,textvar = txt)
#/hCanv
header.pack(fill=tk.X,side=tk.TOP)
#/header


#body
body = tk.Frame(master = root,bg = 'grey')
body.pack(side = tk.BOTTOM,fill=tk.X)



style = ttk.Style(root)#???
style.configure('lefttab.TNotebook', tabposition='en')#???
notebook = ttk.Notebook(master = body, style='lefttab.TNotebook')#???
notebook.pack()





f1 = makeCanv(notebook)
#f1 = tk.Frame(notebook, bg='red', width=200, height=200)#HOME #Raumnummer und wer da sitzt // Bilder wer da sitzt
f2 = tk.Frame(notebook, bg='blue', width=200, height=200)#TimeTable
f3 = tk.Frame(notebook, bg='green', width=200, height=200)#info

F3text = tk.StringVar()
F3text.set('<...>')
F3Label = tk.Label(master = f3,textvariable = F3text,font = myFont1)
F3Label.pack()

f4 = makeOscar(notebook)                                  




f1.bind("<B1-Motion>", clickFrame)
f2.bind("<B1-Motion>",quit)

notebook.add(f1, text='HOME')
notebook.add(f2, text='INFO')
notebook.add(f3, text='Frame 3')
notebook.add(f4, text='OSCAR')





'''BODY
#Will replace Notebook later


#buttonFrame
ButtonFrame = tk.Frame(master = body,bg = 'cyan',height = ScreenWidth-header.winfo_height())
ButtonFrame.pack(fill = tk.Y,side=tk.RIGHT)

#Button1:Home

buttonHome = tk.Label(master = ButtonFrame,text = 'Home')
buttonHome.pack(side = tk.TOP)
#/Button1:Home
#Button2:Info
buttonInfo = tk.Label(master = ButtonFrame,text = 'Info' )
buttonInfo.pack()
#/Button2:Info



#/buttonFrame
mainFrame = tk.Frame(master = body,bg = 'blue')
mainFrame.pack(side=tk.LEFT)




#/body

'''
'''
low_bar = tk.Frame(master = root,bg = 'blue');#height = 300,width = 800,
low_bar.pack()


#tk labels top_bar
canvasx=95
canvasy=95
topCanv = tk.Canvas(master = top_bar,height = canvasy,width = canvasx,bg = 'white')

gif1 = tk.PhotoImage(file='hsrm_logo.gif')
topCanv.create_image(canvasx/2, canvasy/2, image=gif1,anchor = tk.CENTER)
'''
'''
topCanv.create_text(1,1,text = '<canvas image:hsrm-logo>',anchor = tk.NW)
topCanv.create_text(canvasx,canvasy,text = '</canvas image:hsrm-logo>',anchor = tk.SE)
'''
'''

topLable = tk.Label(master = top_bar,text = 'A 127',font = myFont1)

topCanv.pack(side = tk.LEFT,fill = tk.X)
topLable.pack()


#tk labels low_bar
lowFrame = tk.Frame(master = low_bar)



lowLable1 = tk.Label(master = lowFrame,text = '<A 123>',font = myFont1 )
lowLable2 = tk.Label(master = lowFrame,text = '<Raumbeschreibung\ntext>',font = myFont2 )
lowLable1.pack(fill = tk.X)
lowLable2.pack()




style = ttk.Style(root)#???
style.configure('lefttab.TNotebook', tabposition='en')#???
notebook = ttk.Notebook(master = low_bar, style='lefttab.TNotebook')#???

f1 = tk.Frame(notebook, bg='red', width=200, height=200)#HOME #Raumnummer und wer da sitzt // Bilder wer da sitzt
f2 = tk.Frame(notebook, bg='blue', width=200, height=200)#TimeTable
#f3 = tk.Frame(notebook, bg='green', width=200, height=200)#info

notebook.add(f1, text='HOME')
notebook.add(f2, text='INFO')
notebook.add(f3, text='Frame 3')



lowFrame.pack(side=tk.LEFT)
notebook.pack()




'''
'''
content = {'top_text':tk.StringVar()}
content['top_text'].set('text:top_text')
'''








'''
notebook_style = ttk.Style(root)
notebook_style.configure('lefttab.TNotebook', tabposition='en')

notebook = ttk.Notebook( master = low_bar, style='lefttab.TNotebook')
f1 = tk.Frame(notebook, bg='grey', width=50, height=200)
f2 = tk.Frame(notebook, bg='lightgrey', width=50, height=200)
notebook.add(f1, text='f1')
notebook.add(f2, text='f2')
notebook.pack()
'''
def startServer():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostbyname(socket.gethostname())
    port = 8000
    serversocket.bind((host,port))
    print('SERVER('+host+','+str(port)+')\nstarted listening')
    serversocket.listen(5)
    
    while 1: #listen to client
        (clientsocket, address) = serversocket.accept()
        print ("connection found!")
        while 1:
            data = clientsocket.recv(1024).decode()
            F3text.set(data)
            print ('message recieved!\nmessage:'+data)
            print('sending back recieved!')
            ack= 'message recieved!'
            clientsocket.send(ack.encode())

if __name__ == "__main__":

    #filename = 'content.json'
    #makeJson(filename)

    #dict = getDict(filename)
    #print(mydict)
    print("main_screen")
    
    threading._start_new_thread(startServer,())
    root.mainloop()
