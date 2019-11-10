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
    elif connect_file_through == '2':ip_to_con_with = self._all_ip[1]
    elif connect_file_through == '3':ip_to_con_with = self._all_ip[2]
    else:raise Exception('choice ' + connect_file_through + ' does not contain an IP address')

    self.con_info = {'con_to_file_through_ip':ip_to_con_with}


  def _connect_(self):
    global DATA, CONNECTION_WITH
    """
    This will follow through with the status of the connection
    """
    os.system('cd')
    # Opening data.json if it exists
    if os.path.exists(os.path.abspath('data.json')):
      is_a_path = True
    if is_a_path == True and self.con_info['con_to_file_through_ip'] in DATA['ip_connectivity_info']:
      if len(DATA['ip_connectivity_info'][self.con_info['con_to_file_through_ip']]) > 1:
        for i in DATA['ip_connectivity_info'][self.con_info['con_to_file_through_ip']]:
          print(f'Connect to file: {i}')
        get_file_to_con_to = input('File #: ')
        if get_file_to_con_to == '1':self.file_ = DATA['ip_connectivity_info'][self.con_info['con_to_file_through_ip']][0]
        if get_file_to_con_to == '2':self.file_ = DATA['ip_connectivity_info'][self.con_info['con_to_file_through_ip']][1]
        print('connection complete. connection with ' + str(self.con_info['con_to_file_through_ip']) + ' to ' + str(self.file_))
        CONNECTION_WITH.append([self.con_info['con_to_file_through_ip'],self.file_])
      else:
        print('connection complete. connection with ' + str(self.con_info['con_to_file_through_ip']) + ' to ' + str(DATA['ip_connectivity_info'][self.con_info['con_to_file_through_ip']][0]))
        CONNECTION_WITH.append([self.con_info['con_to_file_through_ip'],DATA['ip_connectivity_info'][self.con_info['con_to_file_through_ip']][0]])
    else:
      if self.con_info['con_to_file_through_ip'] == self.IP:
        print('connection complete. connection with ' + self.con_info['con_to_file_through_ip'] + ' to ' + self.data['use'][self.con_info['con_to_file_through_ip']+'_con_to_file_'])
        CONNECTION_WITH.append([self.con_info['con_to_file_through_ip'],self.data['use'][self.con_info['con_to_file_through_ip']+'_con_to_file_']])
      else:
        raise ConnectionError("Can't connect to a file through ip " + self.con_info['con_to_file_through_ip'])
        CONNECTION_WITH.append(['connection to ' + self.con_info['con_to_file_through_ip'] + ' failed'])

    file_info = {'ip_connection_data':{'IP':CONNECTION_WITH[0][0],'connect_to_file':CONNECTION_WITH[0][1]},'file_connection_data':{'FILE':CONNECTION_WITH[0][1],'connect_to_ip':CONNECTION_WITH[0][0]}}

    with open('complete_connection.json','w') as file:
      to_json = json.dumps(file_info,indent=2,sort_keys=False)
      file.write(to_json)
      file.close()
  
    subprocess.call('exit 1',shell=True)
  
  def _return_file_(self):

    "returns the file we are using as the gathering point for data transfering"
    
    open_ = json.loads(open('complete_connection.json','r').read())
    return open_['ip_connection_data']['connect_to_file']
