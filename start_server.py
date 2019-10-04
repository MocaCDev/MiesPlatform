import subprocess, os, json, socket
from colorama import *
from time import sleep as s
from start_client import *

# This will setup connection from client
FROM = ""
HAS_CONNECTED = False
MSG = ""
CON_TO = ""
STARTED = False
RECEIVED_MSG = ""
#IP = ""

def receiveMSG(msg):
  global RECEIVED_MSG

  if len(msg) > 0:
    RECEIVED_MSG = msg
  else:
    pass

def makefile(data):
  with open('server.json','w') as file:
    to_json = json.dumps(data,sort_keys=False)
    file.write(to_json)
    file.close()

def gather(from_,msg,con_to):
  global FROM, MSG, HAS_CONNECTED, CON_TO
  
  FROM += f"('{from_}')<:>('{socket.gethostname()}')\n"
  MSG += f"Message from {FROM}: {msg}"
  HAS_CONNECTED = True
  CON_TO = con_to

def received_msg():
  global FROM, MSG
  print(f'{MSG}')

def client_started(has_started):
  global STARTED

  if has_started == True:
    STARTED = has_started
  else:
    pass

class server:
  def __init__(self,ip,port):
    global HAS_CONNECTED,CON_TO,STARTED
    self.has_connected = HAS_CONNECTED
    self.ip = ip
    self.port = port
    self.has_connected_to = CON_TO
    self.client_started = STARTED
  
  def start(self):
    data = {'ip':self.ip,'port':self.port}
    makefile(data)
    if os.path.exists('server.json'):
      self.server_has_started = True
  
  def _conName_(self):
    return FROM
  
  def _receive_(self,con_msg):
    self.msg_to_show = con_msg
  
  def _establish_(self,accepting):
    #global IP
    #IP = self.ip
    if self.server_has_started:
      print(Fore.GREEN+Style.BRIGHT+'[+]' + Fore.WHITE + ' Server established..awaiting other connections')
      server_ready(self.server_has_started,accepting,self.ip)
    while self.server_has_started:
      if self.client_started:
        if self.has_connected and self.has_connected_to == self.ip:
          s(3)
          print(self.msg_to_show)
          received_msg()
          receiveMSG()
          self.has_connected = False
      else:
        continue
