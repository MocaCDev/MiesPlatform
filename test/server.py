from start_server import *

def using():
  s = server('127.0.0.1',3001)
  s._open_socket_()
  s.accepting()
