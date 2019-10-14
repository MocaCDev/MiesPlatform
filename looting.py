"This file is the looting point for connections to and from the IP address"
import os, json, subprocess
from colorama import Fore,Style
from time import sleep as s

# This will be the connection names
CONNECTION_WITH = []
# This will get extra info from the IP address
DATA = ""

def _get_extra_(extra):
  global DATA
  DATA = extra

class connect:
  
  "deals with all of the connections"

  def _gather_(self,_ip_,all_ip,**DATA):
    "Gather basic data needed to start up the connection"
    self.data = DATA
    self.IP = _ip_
    self._all_ip = all_ip
  
  def _start_(self):
    """
    This will gather the IP address of which the user wants to connect to
    depending on whether or not the given IP address has a linked file to it
    """
    print(Fore.GREEN+Style.BRIGHT+'[+]'+Fore.WHITE+' Setup IP done...')
    s(4)
    print(Style.BRIGHT+Fore.RED+'[-]'+Fore.WHITE+' Connection to IP not complete..\n\nLoading...')
    s(5)
    
    os.system('clear')
    for i in self._all_ip:
      print(Style.BRIGHT+Fore.GREEN+'Connect With IP: ' + Fore.WHITE+i)
      s(.8)

    connect_file_through = input('\nConnect to file through ip [1,2,3] >> ')

    if connect_file_through == '1':ip_to_con_with = self._all_ip[0]
    if connect_file_through == '2':ip_to_con_with = self._all_ip[1]
    if connect_file_through == '3':ip_to_con_with = self._all_ip[2]

    self.con_info = {'con_to_file_through_ip':ip_to_con_with}


  def _connect_(self):
    global DATA
    """
    This will follow through with the status of the connection
    """
    # Opening data.json if it exists
    if os.path.exists(os.path.abspath('data.json')):
      is_a_path = True
    if is_a_path == True and self.con_info['con_to_file_through_ip'] in DATA:
      print('connection complete. connection with ' + str(self.con_info['con_to_file_through_ip']) + ' to ' + str(DATA[self.con_info['con_to_file_through_ip']][0]))
    else:
      if self.con_info['con_to_file_through_ip'] == self.IP:
        print('connection complete. connection with ' + self.con_info['con_to_file_through_ip'] + ' to ' + self.data['use'][self.con_info['con_to_file_through_ip']+'_con_to_file_'])
      else:
        print("Can't connect to a file through ip " + self.con_info['con_to_file_through_ip'])
