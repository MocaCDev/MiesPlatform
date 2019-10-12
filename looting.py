"this file will deal with all of the connections"
import os, json, subprocess
from colorama import Fore,Style
from time import sleep as s

# This will append the ip's from mies_net.py file
IP = []
# This will be the connection names
CONNECTION_WITH = []

class connect:

  def _gather_(self,_ip_,all_ip,**DATA):
    self.data = DATA
    self.IP = _ip_
    self._all_ip = all_ip
  
  def _start_(self):
    print(Fore.GREEN+Style.BRIGHT+'[+]'+Fore.WHITE+' Setup IP done...\n\n')
    s(4)
    print(Style.BRIGHT+Fore.RED+'[-]'+Fore.WHITE+' Connection to IP not complete..\n\n\nLoading...')
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
    if self.con_info['con_to_file_through_ip'] == self.IP:
      print('connection complete. connection with ' + self.con_info['con_to_file_through_ip'] + ' to ' + self.data['use'][self.con_info['con_to_file_through_ip']+'_con_to_file_'])
    else:
      print("Can't connect to a file through ip " + self.con_info['con_to_file_through_ip'])
