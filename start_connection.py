import subprocess, os, json, socket
from time import sleep as s
from colorama import *
from start_server import _

MAIN_IP = ""

class start_connection:
  def __init__(self,startup_ip,startup_port):
    global MAIN_IP
    self.ip = startup_ip
    self.port = startup_port
    # False due to there is no established connection
    self.listening = False
  
    MAIN_IP = self.ip
  
  def start(self):
    DATA = {'ip':self.ip,'port':self.port}
    with open('start_con.json','w') as file:
      to_json = json.dumps(DATA,indent=2,sort_keys=False)
      file.write(to_json)
      file.close()
    s(2)
    print(Fore.GREEN+Style.BRIGHT+'[ + ]' + Fore.WHITE + ' Created ip ' + self.ip + ' with connection port ' + str(self.port))
  
  def _establish_(self,accepting):
    self.listening = accepting
    s(3)
    print(Fore.GREEN+Style.BRIGHT+'[ + ]' + Fore.WHITE + ' Established. Waiting for other connections..')
    _(self.listening)
