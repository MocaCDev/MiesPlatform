from .start_connection import *
from server import using

con = start_connection('127.0.0.1',4001)
con.start()
con._establish_(accepting=True)

using()
