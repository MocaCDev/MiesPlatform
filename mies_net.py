import subprocess, os, json
from time import sleep as s
from colorama import Fore, Style
from looting import connect, _get_extra_
from database import database

l = connect()
d = database()

IP = [
  "127.0.0.1",
  "109.0.4.8",
  "130.8.9.1"
]
CONNECTIONS = []
# The IP connection will be linked with a key so that another IP address can connect to the active IP address and send/receive information
IP_KEYS = {}
default_keys = [
  'default_01',
  'aub87yu',
  'uyghb89',
  'ughji89',
  'auuouhj'
]

def _write_to_file_(path,found_in,name_of_warning):
  if '.yaml' in path:
    msg = f'Message:\n  -{found_in[name_of_warning]}'
  elif '.json' in path:
    msg = json.dumps({'message':found_in[name_of_warning]},indent=True,sort_keys=False)
  else:
    msg = found_in[name_of_warning]
  if open(path,'r').read() != '':
    old_info = open(path,'r').read()
    with open('old_info.txt','w') as file:
      file.write(old_info)
      file.close()
  with open(path,'w') as file:
    file.write(msg)
    file.close()

def _raise_error_(t):
  raise Exception('These names are data files for the application:\ndata.txt\ndata.json\ncomplete_connection.json\n\nOops sorry, we cannot use ' + t + ' as a data file')

class mies_network:

  def _make_fields_(self):
    self.path = os.environ.get('HOME')
    self.info = {}
    d._setup_sql_database_()
    return True

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
          os.system(f'clear && cd {self.path} && echo "\n" && ls')
          folder_name = input('\nName of folder which contains the file: ')
          if folder_name != '':
            self.path = self.path + '/' + folder_name
            os.system(f'cd {os.path.abspath(self.path)} && echo "\n" && ls')
          else:
            os.system('clear && cd && echo "\n" && ls')
          file_name = input(f'File {i+1}: ')
          if file_name == 'data.txt':_raise_error_(file_name)
          if file_name == 'data.jsn':_raise_error_(file_name)
          if file_name == 'complete_connection.json':_raise_error_(file_name)
          self.path = os.path.join(self.path, file_name)
          d.append(self.path)
        if not os.path.exists(os.path.abspath(d[0])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[0]))
        if not os.path.exists(os.path.abspath(d[1])):raise NotADirectoryError('No such directory ' + os.path.abspath(d[1]))
        if os.path.exists(os.path.abspath(d[0])) and os.path.exists(os.path.abspath(d[1])):self.info.update({'ip_connectivity_info':{IP[0]:[os.path.abspath(d[0])],IP[1]:[os.path.abspath(d[1])]},'file_connectivity_info':{os.path.abspath(d[0]):[IP[0]],os.path.abspath(d[1]):[IP[1]]}})
      elif how_many == '3':
        for i in range(3):
          self.path = os.environ.get('HOME')
          os.system(f'clear && cd {self.path} && echo "\n" && ls')
          folder_name = input('\nName of folder which contains the file: ')
          if folder_name != '':
            self.path = self.path + '/' + folder_name
            os.system(f'cd {os.path.abspath(self.path)} && echo "\n" && ls')
          else:
            os.system('clear && cd && echo "\n" && ls')
          file_name = input(f'File {i+1}: ')
          if file_name == 'data.txt':_raise_error_(file_name)
          if file_name == 'data.json':_raise_error_(file_name)
          if file_name == 'complete_connection.json':_raise_error_(file_name)
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
        if self.ip in self.info['ip_connectivity_info']:
          self.info['ip_connectivity_info'][self.ip].append(self.file_path)
        else:
          self.info['ip_connectivity_info'].update({self.ip:[self.file_path]})
        if not 'file_connectivity_info' in self.info:
          self.info.update({'file_connectivity_info':{os.path.abspath(setup_info['PATH']):[self.ip]}})
        elif 'file_connectivity_info' in self.info:
          if not os.path.abspath(setup_info['PATH']) in self.info['file_connectivity_info']:
            self.info['file_connectivity_info'].update({os.path.abspath(setup_info['PATH']):[self.ip]})
          if not self.ip in self.info['file_connectivity_info'][os.path.abspath(setup_info['PATH'])]:
            self.info['file_connectivity_info'][os.path.abspath(setup_info['PATH'])].append(self.ip)
        ip_con_to_file = {self.ip+'_con_to_file_':os.path.abspath(setup_info['PATH'])}
        self.path_ = setup_info['PATH']
      else:
        raise Exception('File ' + os.path.abspath(setup_info['PATH']) + ' does not exists')
    if 'create_path' in setup_info:
      self.open_file = open(setup_info['create_path'],'w')
      self.open_file.close()
      if self.ip in self.info['ip_connectivity_info']:
        self.info['ip_connectivity_info'][self.ip].append(os.path.abspath(setup_info['create_path']))
      else:
        self.info['ip_connectivity_info'].update({self.ip:[os.path.abspath(setup_info['create_path'])]})
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
    d._insert_into_table_(1,IP=[self.ip],FILE=self.info['ip_connectivity_info'][self.ip])
  
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

    os.system('clear')

    # Messages written into the file the user has created or is using
    warn_messages = {
      'default':'This file is the gathering point of data being pulled from other files',
      'warning':'NOTE: This is the gathering point for data from other files, if you write in this file it will be transfered to old_info.txt',
      'custom':''
      }

    "sets up the information for the file that will store data"

    self.FILE_INFO = {}
    get_amount_of_bytes = int(input('Amount of bytes the file will accept from other bytes (must be 1000 and up) >> '))
    if get_amount_of_bytes < 1000:
      raise Exception(str(get_amount_of_bytes) + ' is too low to store much, if any, data')
    if get_amount_of_bytes > 999:
      self.FILE_INFO.update({'total_bytes':get_amount_of_bytes})
      self.info.update({'using':{'ip':self.info['file_connectivity_info'][self.path_][0],'file':l._return_file_()}})
      self.info['using'].update(self.FILE_INFO)
      with open('data.json','w') as file:
        to_json = json.dumps(self.info,indent=2,sort_keys=False)
        file.write(to_json)
        file.close()
    warn_type = input("Warning Type [default,warning,custom] >> ")
    if warn_type == 'default':
      _write_to_file_(self.path_,warn_messages,warn_type)
    elif warn_type == 'warning':
       _write_to_file_(self.path_,warn_messages,warn_type)
    elif warn_type == 'custom':
      custom_warn = input('Custom Message >> ')
      warn_messages['custom'] = custom_warn
      _write_to_file_(self.path_,warn_messages,warn_type)
    else:
      raise Exception('The choice ' + warn_type + ' is not a valid choice')
  
  def _START_CONNECTION_(self):
    "used in other files to connect with ip"
    l._start_()
    l._connect_()
  
  def _append_connections_(self):

    "will append network information for file connections"

    get_data = json.loads(open('data.json','r').read())
    con_data = json.loads(open('complete_connection.json','r').read())
    
    if get_data['using']['ip'] == con_data['ip_connection_data']['IP']:
      os.system('clear')
      print('Connection has been established, IP ' + get_data['using']['ip'] + ' in use with file ' + get_data['using']['file'] + f'\nOld Info: {open("old_info.txt","r").read()}\nTRANSFERED INTO: old_info.txt' + '\n\nWARNING:\n' + open(get_data['using']['file'],'r').read())
      s(4.2)
      subprocess.call('clear',shell=True)
    if not 'ip_key' in get_data['using']:
      for i in range(len(IP)):
        if IP[i] in get_data['ip_connectivity_info']:
          get_key = input('\nKey for IP ' + IP[i] + '[press enter if you want a default key] >> ')
          if get_key == '':
            get_key = default_keys[0]
            del(default_keys[0])
          get_data['ip_connectivity_info'][IP[i]].append({'ip_key':get_key})
          for j in get_data['file_connectivity_info']:
            if j in get_data['ip_connectivity_info'][IP[i]]:
              get_data['file_connectivity_info'][j] = IP[i],{'ip_key':get_key}
              #print(get_data['file_connectivity_info'][j])
              IP_KEYS.update({IP[i]:get_key})
          
          if len(get_data['ip_connectivity_info'][IP[i]]) == 1:
            print(IP[i] + ' connects to ' + get_data['ip_connectivity_info'][IP[i]][0])
          else:
            print(IP[i] + ' connects to ' + str(get_data['ip_connectivity_info'][IP[i]]))
          if IP[i] == get_data['using']['ip']:
            get_data['using'].update({'ip_key':get_key})
          else:
            if get_data['using']['file'] in get_data['ip_connectivity_info'][IP[i]]:
              get_data['using'].update({'ip_key':get_key})

          with open('data.json','w') as file:
            to_json = json.dumps(get_data,indent=2,sort_keys=False)
            file.write(to_json)
            file.close()
