from mies_net import *
import os
from time import sleep as s
from colorama import Fore, Style
from mies_net import mies_network

s = mies_network()

def _raise_using_error_(t):
  raise Exception('These names are data files for the application:\ndata.txt\ndata.json\ncomplete_connection.json\n\nOops sorry, we cannot use ' + t + ' as a data file')
def _raise_create_error_(t):
  raise Exception('These names are data files for the application:\ndata.txt\ndata.json\ncomplete_connection.json\n\nOops sorry, we cannot create a file of name ' + t)

s._make_fields_()

MAIN_PATH = os.environ.get('HOME')

if not os.path.isfile(os.path.abspath('data.json')) or not os.path.isfile(os.path.abspath('complete_connection.json')):
  s._set_ip_()

  type_ = input(Fore.CYAN + '\nCreate file or use existing[c,u]: ')

  if type_ == 'c':
    file_to_create = input(Fore.BLUE + 'Create file: ')
    if file_to_create == 'data.txt':_raise_create_error_(file_to_create)
    if file_to_create == 'data.json':_raise_create_error_(file_to_create)
    if file_to_create == 'complete_connection.json':_raise_create_error_(file_to_create)
    check_path = os.path.join(MAIN_PATH,file_to_create)
    if os.path.exists(check_path):
      raise Exception("Path " + os.path.abspath(file_to_create) + " already exists\n\n" + "File Reader Gathered:\n " + open(os.path.abspath(file_to_create),'r').read())
    s._gather_(create_path=file_to_create)
    s._establish_('created ' + os.path.abspath(file_to_create),s._return_ip_())
  elif type_ == 'u':
    os.system(f'clear && cd {MAIN_PATH} && echo "\n" && ls')
    folder_name = input('\nName of folder which contains the file: ')
    if '.gf' in folder_name:
      os.system('cd MiesPlatform')
      if os.path.isfile(MAIN_PATH + '/MiesPlatform/Con_Files' + '/' + folder_name):
        op = open(MAIN_PATH + '/MiesPlatform/Con_Files' + '/' + folder_name,'r').read()
        MAIN_PATH = MAIN_PATH + op
        if os.path.isfile(MAIN_PATH):
          s._gather_(PATH=MAIN_PATH)
          s._establish_('connected to ' + MAIN_PATH,s._return_ip_())
        else:
          raise FileExistsError('The file ' + MAIN_PATH + ' does not exists')
      else:
        print('Cannot find ' + folder_name + ' in ' + os.path.abspath('Con_Files'))
    else:
      if folder_name != '':
        MAIN_PATH = MAIN_PATH + '/' + folder_name
        os.system(f'cd {os.path.abspath(MAIN_PATH)} && echo "\n" && ls')
      else:
        os.system(f'clear && cd {MAIN_PATH} ' + '&& echo "\n" && ls')
      file_name = input(Fore.BLUE + 'Existing Filename: ')
      if file_name == 'data.txt':_raise_using_error_(file_name)
      if file_name == 'data.json':_raise_using_error_(file_name)
      if file_name == 'complete_connection.json':_raise_using_error_(file_name)
      _PATH_ = os.path.join(MAIN_PATH,file_name)
      s._gather_(PATH=_PATH_)
      s._establish_('connected to ' + os.path.abspath(file_name),s._return_ip_())
  else:
    raise Exception('The choice ' + type_ + ' is not a valid choice')
  s._START_CONNECTION_()
  s.file_info()
if os.path.isfile(os.path.abspath('data.json')) and os.path.isfile(os.path.abspath('complete_connection.json')):
  s._append_connections_()
