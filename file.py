from mies_net import *
import os
from time import sleep as s

s = mies_network()

s._set_ip_()

type_ = input('Create file or use existing[c,u]: ')

if type_ == 'c':
  file_to_create = input('Create file: ')
  s._gather_(create_path=file_to_create)
  s._establish_('created ' + os.path.abspath(file_to_create))
if type_ == 'u':
  file_name = input('Existing Filename: ')
  s._gather_(PATH=file_name)
  s._establish_('connected to ' + os.path.abspath(file_name))
