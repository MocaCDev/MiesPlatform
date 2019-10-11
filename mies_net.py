import subprocess, os, json
from time import sleep as s

IP = [
  "127.0.0.1",
  "109.0.4.8",
  "130.8.9.1"
]

class mies_network:

  # MiesPlatform will run off of this IP
  def _set_ip_(self):
    global IP
    for i in IP:
      print('IP: ' + i)
    get_ip = input('Which Ip would you like to use? [1,2,3] ')
    if get_ip == '1':ip = f'{IP[0]}'
    if get_ip == '2':ip = f'{IP[1]}'
    if get_ip == '3':ip = f'{IP[2]}'
    self.ip = str(ip)

  # Sets up information about location of data storage
  def _gather_(self,**setup_info):
    if 'PATH' in setup_info:
      if os.path.exists(setup_info['PATH']):
        self.file_path = os.path.abspath(setup_info['PATH'])
      else:
        raise Exception('File ' + os.path.abspath(setup_info['PATH']) + ' does not exists')
    if 'create_path' in setup_info:
      self.open_file = open(setup_info['create_path'],'w')
      self.open_file.close()
    self.setup = setup_info
  
  def _establish_(self,*data):
    self.data = str(data)
    with open('data.txt','w') as file:
      file.write(self.data + "\nIP: " + f"('{self.ip}')")
      file.close()
    
    if 'PATH' in self.setup:
      if os.path.exists(self.setup['PATH']):
        s(3)
        print('Successfully connected to ' + os.path.abspath(self.setup['PATH']))
    if 'create_path' in self.setup:
      if os.path.exists(self.setup['create_path']):
        s(3)
        print('Successfully created ' + os.path.abspath(self.setup['create_path']))
