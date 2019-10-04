import os, subprocess, socket, json
from start_server import *

READY = False
ACCEPTING = False
IP = ""

def updFile(with_data):
  with open('server.json','w') as file:
    to_json = json.dumps(with_data,sort_keys=False)
    file.write(to_json)
    file.close()

def server_ready(is_ready,server_accepting,ip):
  global READY,ACCEPTING,IP

  if server_accepting:
    ACCEPTING = server_accepting
    IP = ip
  else:
    pass

  if is_ready == True:
    READY = is_ready
  else:
    pass

class client:
  def __init__(self,use_ip,use_port):
    global READY,ACCEPTING,IP
    self.use_ip = use_ip
    self.is_ready = READY
    self.use_port = use_port
    self.server_ready = ACCEPTING
    self.ip = IP
  
  def send(self,to_file,msg):
    while self.server_ready:
      if self.use_ip == self.ip and self.server_ready:
        i = input('Name: ')
        receiveMSG(i)
        self.server_ready = False
        

  def _establish_(self):
    if self.use_ip == self.ip:
      NEW_DATA = {'con_ip':self.use_ip,'connect_to':self.ip}
      updFile(NEW_DATA)
