import subprocess, os, json
from time import sleep as s
from colorama import Fore, Style
from looting import connect, _get_extra_

l = connect()

IP = [
  "127.0.0.1",
  "109.0.4.8",
  "130.8.9.1"
]
CONNECTIONS = []

class mies_network:

  print(Fore.RED + Style.BRIGHT + '[-]' + Fore.WHITE + ' Setup IP not complete...')
  print(Style.BRIGHT + Fore.RED + '[-]' + Fore.WHITE + ' Connectino to IP not complete...')
  print('\n\n')
  s(3.6)

  # MiesPlatform will run off of this IP
  def _set_ip_(self):
    global IP
    for i in IP:
      print(Style.BRIGHT + Fore.GREEN + 'IP: ' + Fore.WHITE+ i)
    
    assign = input('Assign files more than one IP?[y/n] ')

    if assign == 'y':
      self.assign = True
      d = []
      how_many = input('How many IP connection >> ')

      if how_many == '1':
        raise Exception('Cannot do 1 connection, must be 2 or 3')
      if how_many == '2':
        for i in range(2):
          file_name = input(f'File {i+1}: ')
          d.append(file_name)
        if not os.path.exists(os.path.abspath(d[0])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[0]))
        if not os.path.exists(os.path.abspath(d[1])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[1]))
        if os.path.exists(os.path.abspath(d[0])) and os.path.exists(os.path.abspath(d[1])):self.info = {IP[0]:[os.path.abspath(d[0])],IP[1]:[os.path.abspath(d[1])]}
      if how_many == '3':
        for i in range(3):
          file_name = input(f'File {i+1}: ')
          d.append(file_name)
        if not os.path.exists(os.path.abspath(d[0])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[0]))
        if not os.path.exists(os.path.abspath(d[1])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[1]))
        if not os.path.exists(os.path.abspath(d[2])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[2]))
        if os.path.exists(os.path.abspath(d[0])) and os.path.exists(os.path.abspath(d[1])) and os.path.exists(os.path.abspath(d[2])):self.info = {IP[0]:[os.path.abspath(d[0])],IP[1]:[os.path.abspath(d[1])],IP[2]:[os.path.abspath(d[2])]}
    else:
      self.assign = False
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
        if self.assign == True and self.ip in self.info:
          self.info[self.ip].append(self.file_path)
        ip_con_to_file = {self.ip+'_con_to_file_':os.path.abspath(setup_info['PATH'])}
      else:
        raise Exception('File ' + os.path.abspath(setup_info['PATH']) + ' does not exists')
    if 'create_path' in setup_info:
      self.open_file = open(setup_info['create_path'],'w')
      self.open_file.close()
      if self.assing == True and self.ip in self.info:
        self.info[self.ip].append(os.path.abspath(setup_info['create_path']))
      ip_con_to_file = {self.ip+'_con_to_file_':os.path.abspath(setup_info['create_path'])}
    self.setup = setup_info
    l._gather_(self.ip,IP,ip_to_con_with=self.ip,use=ip_con_to_file)
  
  def _establish_(self,*data):
    data += tuple(f'{self.ip}')
    self.data = str(data)
    with open('data.txt','w') as file:
      file.write(self.data)
      file.close()
    
    if 'PATH' in self.setup:
      if os.path.exists(self.setup['PATH']):
        if self.assign == True:
          with open('data.json','w') as file:
            data = self.info
            to_json = json.dumps(data,indent=2,sort_keys=False)
            file.write(to_json)
            file.close()
          _get_extra_(self.info)
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
