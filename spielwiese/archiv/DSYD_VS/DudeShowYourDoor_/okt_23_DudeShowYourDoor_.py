
import tkinter as tk
from tkinter import ttk
import json
from datetime import datetime

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

myFont1 = ('Arial',30)
myFont2 = ('Arial',20)

## tkwindow
root = tk.Tk() #root: window main frame instance
#root.overrideredirect(1) # no bar on top 

##tkframesToplevel
top_bar = tk.Frame(master = root);#height = 100,width = 800
top_bar.pack()
low_bar = tk.Frame(master = root,bg = 'blue');#height = 300,width = 800,
low_bar.pack()


#tk labels top_bar
canvasx=95
canvasy=95
topCanv = tk.Canvas(master = top_bar,height = canvasy,width = canvasx,bg = 'white')

gif1 = tk.PhotoImage(file='hsrm_logo.gif')
topCanv.create_image(canvasx/2, canvasy/2, image=gif1,anchor = tk.CENTER)
'''
topCanv.create_text(1,1,text = '<canvas image:hsrm-logo>',anchor = tk.NW)
topCanv.create_text(canvasx,canvasy,text = '</canvas image:hsrm-logo>',anchor = tk.SE)
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
#notebook.add(f3, text='Frame 3')



lowFrame.pack(side=tk.LEFT)
notebook.pack()




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




if __name__ == "__main__":
        #filename = 'content.json'
        #makeJson(filename)

        #dict = getDict(filename)
        #print(mydict)
        print("hello World")
        
        root.mainloop()
