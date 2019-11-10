import socket
import json
# gui mit submit genau so vom layout wie die echte app
class Server():
   #reference: https://realpython.com/python-sockets/
   def __init__(self):
      self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# s = server
      host =socket.gethostbyname(socket.gethostname())
      port =8000
      print('connecting to server:'+(str(host)+' '+str(port)))
      self.server.connect((host,port))
      print('connected to server\ntype message:')
   

   def push_message(self,msg):
      self.server.send(msg.encode()) 
      data = ''
      data = self.server.recv(1024).decode()
   
      print (data)

def makeJson(filename):
      #make a dictionary
      # {<key>:<value>} dict
      # [<listelem0>,<listelem1>,...] list
      # (<elem1>,<elem2>) tuple
      mydict = {'key1':'value1'}
        
      #make a jsonfile from mydict
      with open(filename,'w') as f:
            json.dump(mydict,f)

def getDictStr(filename):
      with open(filename) as f: 
            str = f.read() 
            #data = json.loads(str) #make a dict from string
            #print(type(jstr))

      return str


server = Server()

filename = 'content.json'
makeJson(filename)

#dict = getDict(filename)
    #print(mydict)
makeJson(filename)
msg = getDictStr(filename)
server.push_message(msg)


server.server.close()
