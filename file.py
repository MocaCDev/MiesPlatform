from mies_net import *
import os
from time import sleep as s
from colorama import Fore, Style
from mies_net import mies_network

s = mies_network()

if not os.path.isfile(os.path.abspath('data.json')):
  s._set_ip_()

  type_ = input(Fore.CYAN + '\nCreate file or use existing[c,u]: ')

  if type_ == 'c':
    file_to_create = input(Fore.BLUE + 'Create file: ')
    if os.path.exists(file_to_create):
      raise Exception("Path " + os.path.abspath(file_to_create) + " already exists\n\n" + "File Reader Gathered:\n " + open(os.path.abspath(file_to_create),'r').read())
    s._gather_(create_path=file_to_create)
    s._establish_('created ' + os.path.abspath(file_to_create))
  if type_ == 'u':
    file_name = input(Fore.BLUE + 'Existing Filename: ')
    s._gather_(PATH=file_name)
    s._establish_('connected to ' + os.path.abspath(file_name))

  s._START_CONNECTION_()
