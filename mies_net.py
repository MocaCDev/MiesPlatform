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

  def _make_fields_(self):
    self.path = os.environ.get('HOME')
    self.info = {}

  # MiesPlatform will run off of this IP
  def _set_ip_(self):

    print(Fore.RED + Style.BRIGHT + '[-]' + Fore.WHITE + ' Setup IP not complete...')
    print(Style.BRIGHT + Fore.RED + '[-]' + Fore.WHITE + ' Connection to IP not complete...')
    print('\n\n')
    s(3.6)

    "Sets up an IP to connect to a file"

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
          self.path = os.environ.get('HOME')
          os.system('clear && cd {self.path} && echo "\n" && ls')
          folder_name = input('\nName of folder which contains the file: ')
          if folder_name != '':
            self.path = self.path + '/' + folder_name
            os.system(f'cd {os.path.abspath(self.path)} && echo "\n" && ls')
          else:
            os.system('clear && cd && echo "\n" && ls')
          file_name = input(f'File {i+1}: ')
          self.path = os.path.join(self.path, file_name)
          d.append(self.path)
        if not os.path.exists(os.path.abspath(d[0])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[0]))
        if not os.path.exists(os.path.abspath(d[1])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[1]))
        if os.path.exists(os.path.abspath(d[0])) and os.path.exists(os.path.abspath(d[1])):self.info.update({'ip_connectivity_info':{IP[0]:[os.path.abspath(d[0])],IP[1]:[os.path.abspath(d[1])]},'file_connectivity_info':{os.path.abspath(d[0]):[IP[0]],os.path.abspath(d[1]):[IP[1]]}})
      elif how_many == '3':
        for i in range(3):
          self.path = os.environ.get('HOME')
          os.system('clear && cd {self.path} && echo "\n" && ls')
          folder_name = input('\nName of folder which contains the file: ')
          if folder_name != '':
            self.path = self.path + '/' + folder_name
            os.system(f'cd {os.path.abspath(self.path)} && echo "\n" && ls')
          else:
            os.system('clear && cd && echo "\n" && ls')
          file_name = input(f'File {i+1}: ')
          self.path = os.path.join(self.path, file_name)
          d.append(self.path)
        if not os.path.exists(os.path.abspath(d[0])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[0]))
        if not os.path.exists(os.path.abspath(d[1])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[1]))
        if not os.path.exists(os.path.abspath(d[2])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[2]))
        if os.path.exists(os.path.abspath(d[0])) and os.path.exists(os.path.abspath(d[1])) and os.path.exists(os.path.abspath(d[2])):self.info.update({'ip_connectivity_info':{IP[0]:[os.path.abspath(d[0])],IP[1]:[os.path.abspath(d[1])],IP[2]:[os.path.abspath(d[2])]},'file_connectivity_info':{os.path.abspath(d[0]):[IP[0]],os.path.abspath(d[1]):[IP[1]],os.path.abspath(d[2]):[IP[2]]}})
      else:raise Exception('There is a max of 3 IP connections available, cannot assign ' + how_many + ' connections')
    elif assign == 'n':self.assign = False
    else:raise Exception('Choice ' + assign + ' is not a valid choice')
    get_ip = input('Which Ip would you like to use? [1,2,3] ')

    # Getting the IP
    if get_ip == '1':ip = f'{IP[0]}'
    elif get_ip == '2':ip = f'{IP[1]}'
    elif get_ip == '3':ip = f'{IP[2]}'
    else:raise Exception('Choice ' + get_ip + ' is not a valid choice')

    if assign == 'n':self.info = {'ip_connectivity_info':{ip:[]}}

    # This will be used for connections across the platform
    self.ip = str(ip)

  def _return_ip_(self):
    return self.ip

  # Sets up information about location of data storage
  def _gather_(self,**setup_info):

    "Gathers information to setup the IP file connection officialy"

    if 'PATH' in setup_info:
      if os.path.exists(setup_info['PATH']):
        self.file_path = os.path.abspath(setup_info['PATH'])
        self.info['ip_connectivity_info'][self.ip].append(self.file_path)
        if not 'file_connectivity_info' in self.info:
          self.info.update({'file_connectivity_info':{os.path.abspath(setup_info['PATH']):[self.ip]}})
        elif 'file_connectivity_info' in self.info:
          if not self.ip in self.info['file_connectivity_info'][os.path.abspath(setup_info['PATH'])]:
            self.info['file_connectivity_info'][os.path.abspath(setup_info['PATH'])].append(self.ip)
        ip_con_to_file = {self.ip+'_con_to_file_':os.path.abspath(setup_info['PATH'])}
        self.path_ = setup_info['PATH']
      else:
        raise Exception('File ' + os.path.abspath(setup_info['PATH']) + ' does not exists')
    if 'create_path' in setup_info:
      self.open_file = open(setup_info['create_path'],'w')
      self.open_file.close()
      self.info['ip_connectivity_info'][self.ip].append(os.path.abspath(setup_info['create_path']))
      if self.ip in self.info['ip_connectivity_info'] and os.path.abspath(setup_info['create_path']) in self.info['ip_connectivity_info'][self.ip]:
        if not 'file_connectivity_info' in self.info:
          self.info.update({'file_connectivity_info':{os.path.abspath(setup_info['create_path']):[]}})
        else:
          self.info['file_connectivity_info'].update({os.path.abspath(setup_info['create_path']):[]})
        if not self.ip in self.info['file_connectivity_info'][os.path.abspath(setup_info['create_path'])]:self.info['file_connectivity_info'][os.path.abspath(setup_info['create_path'])].append(self.ip)
      ip_con_to_file = {self.ip+'_con_to_file_':os.path.abspath(setup_info['create_path'])}
      self.path_ = setup_info['create_path']
    self.setup = setup_info
    l._gather_(self.ip,IP,ip_to_con_with=self.ip,use=ip_con_to_file)
  
  def _establish_(self,*data):

    "Establishes connection between IP and file"

    
    self.data = str(data)
    with open('data.txt','w') as file:
      file.write(self.data)
      file.close()
    
    if 'PATH' in self.setup:
      if os.path.exists(self.setup['PATH']):
        with open('data.json','w') as file:
          data = self.info
          to_json = json.dumps(data,indent=2,sort_keys=False)
          file.write(to_json)
          file.close()
        _get_extra_(self.info)
        s(3)
        print('Successfully connected  ' + str(self.info['ip_connectivity_info'][self.ip]) + ' to IP address ' + self.ip)
    if 'create_path' in self.setup:
      if os.path.exists(self.setup['create_path']):
        with open('data.json','w') as file:
          data = self.info
          to_json = json.dumps(data,indent=2,sort_keys=False)
          file.write(to_json)
          file.close()
        _get_extra_(self.info)
        s(3)
        print('Successfully created ' + os.path.abspath(self.setup['create_path']) + " \nSuccessfully connected " + str(self.info['ip_connectivity_info'][self.ip]) + " to IP address " + self.ip)
        subprocess.call('exit 1', shell=True)
  
  def file_info(self):

    global INFO

    "sets up the information for the file that will store data"

    self.FILE_INFO = {}
    get_amount_of_bytes = int(input('Amount of bytes the file will accept from other bytes (must be 1000 and up) >> '))
    if get_amount_of_bytes < 1000:
      raise Exception(str(get_amount_of_bytes) + ' is too low to store much, if any, data')
    if get_amount_of_bytes > 999:
      self.FILE_INFO.update({'total_bytes':get_amount_of_bytes})
      self.info.update({'using':{'ip':self.info['file_connectivity_info'][self.path_][0],'file':self.info['ip_connectivity_info'][self.ip][0]}})
      self.info['using'].update(self.FILE_INFO)
      with open('data.json','w') as file:
        to_json = json.dumps(self.info,indent=2,sort_keys=False)
        file.write(to_json)
        file.close()
  
  def _START_CONNECTION_(self):
    "used in other files to connect with ip"
    l._start_()
    l._connect_()
