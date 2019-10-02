from start_connection import *
import server

con = start_connection('127.0.0.1',4001)
con.start()
con._establish_(accepting=True)

using()
