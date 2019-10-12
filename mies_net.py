import subprocess, os, json
from time import sleep as s
from colorama import Fore, Style
from looting import *

l = connect()

IP = [
  "127.0.0.1",
  "109.0.4.8",
  "130.8.9.1"
]
CONNECTIONS = []

class mies_network:

  # MiesPlatform will run off of this IP
  def _set_ip_(self):
    global IP
    for i in IP:
      print(Style.BRIGHT + Fore.GREEN + 'IP: ' + Fore.WHITE+ i)
    get_ip = input('Which Ip would you like to use? [1,2,3] ')

    # Getting the IP
    if get_ip == '1':ip = f'{IP[0]}'
    if get_ip == '2':ip = f'{IP[1]}'
    if get_ip == '3':ip = f'{IP[2]}'

    # This will be used for connections across the platform
    self.ip = str(ip)

  # Sets up information about location of data storage
  def _gather_(self,**setup_info):
    if 'PATH' in setup_info:
      if os.path.exists(setup_info['PATH']):
        self.file_path = os.path.abspath(setup_info['PATH'])
        ip_con_to_file = {self.ip+'_con_to_file_':os.path.abspath(setup_info['PATH'])}
      else:
        raise Exception('File ' + os.path.abspath(setup_info['PATH']) + ' does not exists')
    if 'create_path' in setup_info:
      self.open_file = open(setup_info['create_path'],'w')
      self.open_file.close()
      ip_con_to_file = {self.ip+'_con_to_file_':os.path.abspath(setup_info['create_path'])}
    self.setup = setup_info
    l._gather_(self.ip,IP,ip_to_con_with=self.ip,use=ip_con_to_file)
  
  def _establish_(self,*data):
    data += ("CONNECT_IP",self.ip)
    self.data = str(data)
    with open('data.txt','w') as file:
      file.write(self.data)
      file.close()
    
    if 'PATH' in self.setup:
      if os.path.exists(self.setup['PATH']):
        s(3)
        print('Successfully connected to ' + os.path.abspath(self.setup['PATH']))
        subprocess.call('exit 1', shell=True)
    if 'create_path' in self.setup:
      if os.path.exists(self.setup['create_path']):
        s(3)
        print('Successfully created ' + os.path.abspath(self.setup['create_path']))
        subprocess.call('exit 1', shell=True)
  
  def _START_CONNECTION_(self):
    "used in other files to connect with ip"
    l._start_()
    l._connect_()
