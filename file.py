from mies_net import *
import os
from time import sleep as s
from colorama import Fore, Style
from mies_net import mies_network

s = mies_network()

MAIN_PATH = os.environ.get('HOME')
print(MAIN_PATH)

if not os.path.isfile(os.path.abspath('data.json')) or not os.path.isfile(os.path.abspath('complete_connection.json')):
  s._set_ip_()

  type_ = input(Fore.CYAN + '\nCreate file or use existing[c,u]: ')

  if type_ == 'c':
    file_to_create = input(Fore.BLUE + 'Create file: ')
    check_path = os.path.join(MAIN_PATH,file_to_create)
    if os.path.exists(check_path):
      raise Exception("Path " + os.path.abspath(file_to_create) + " already exists\n\n" + "File Reader Gathered:\n " + open(os.path.abspath(file_to_create),'r').read())
    s._gather_(create_path=file_to_create)
    s._establish_('created ' + os.path.abspath(file_to_create))
  elif type_ == 'u':
    os.system('clear && cd')
    os.system('echo "\n" && ls')
    folder_name = input('\nName of folder which contains the file: ')
    if folder_name != '':
      MAIN_PATH = MAIN_PATH + '/' + folder_name
      os.system(f'cd {os.path.abspath(MAIN_PATH)} && echo "\n" && ls')
    else:
      os.system('cd && echo "\n" && ls')
    file_name = input(Fore.BLUE + 'Existing Filename: ')
    _PATH_ = os.path.join(MAIN_PATH,file_name)
    s._gather_(PATH=_PATH_)
    s._establish_('connected to ' + os.path.abspath(file_name))
  else:
    raise Exception('The choice ' + type_ + ' is not a valid choice')
  s._START_CONNECTION_()
if os.path.isfile(os.path.abspath('data.json')) and os.path.isfile(os.path.abspath('complete_connection.json')):
  pass
