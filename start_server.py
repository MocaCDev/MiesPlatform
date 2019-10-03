import subprocess, os, json, socket
from colorama import *
from time import sleep as s

# This will setup connection from client
FROM = ""
HAS_CONNECTED = False
MSG = ""
CON_TO = ""
STARTED = False

def makefile(data):
  with open('start_server.json','w') as file:
    to_json = json.dumps(data,sort_keys=False)
    file.write(to_json)
    file.close()

def gather(from_,msg,con_to):
  global FROM, MSG, HAS_CONNECTED, CON_TO
  
  FROM += f"Established connection with ('{from_}')<:>('{socket.gethostname()}')\n"
  MSG += f"Connection {from_} gives: {msg}\n"
  HAS_CONNECTED = True
  CON_TO = con_to

def gathered():
  global FROM, MSG
  print(f'{FROM}')
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
    if os.path.exists('start_server.json'):
      self.server_has_started = True
  
  def _establish(self,accepting):
    if self.server_has_started:
      print(Fore.GREEN+Style.BRIGHT+'[+]' + Fore.WHITE + ' Server established..awaiting other connections')
    while self.server_has_started:
      if self.client_started:
        if self.has_connected and self.has_connected_to == self.ip:
          s(3)
          gathered()
          self.has_connected = False
      else:
        continue
