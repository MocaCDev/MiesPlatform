import subprocess, os, json, socket
from time import sleep as s
import colorama

has_established = ""

def _(has_est):
  has_established = has_est

class server:
  def __init__(self,con_to_ip,with_port):
    self.con_to = con_to_ip
    self.use_port = with_port
  
  def _open_socket_(self):
    if has_established:
      return True
  
  def accepting(self):
    print('Accepted from ' + socket.gethostname())
    return True
