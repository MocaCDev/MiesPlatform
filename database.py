import sqlite3, os

class database:

  "this will store data about ip, file, user and password in a sql database"

  def _setup_sql_database_(self):

    "setting db server to true"

    self.db_server = True
    # PATH TO database.db
    self.PATH = os.path.abspath('database.db')
  
  def _insert_into_table_(self,id_,**INFO):

    "Creates the MiesPlatform SQL Database with sqlite3"

    with open('database.sql','w') as file:
      connect = sqlite3.connect(self.PATH)
      crs = connect.cursor()

      if len(INFO['FILE']) > 1:
        file.write(f"""
CREATE TABLE IP_INFO(
  ACTIVE_ID INTEGER PRIMARY KEY,
  ACTIVE_IP TEXT NOT NULL,
  ACTIVE_FILE_DIR TEXT NOT NULL
);

INSERT INTO IP_INFO(ACTIVE_ID,ACTIVE_IP,ACTIVE_FILE_DIR)
VALUES ({id_},'{INFO["IP"][0]}','{INFO["FILE"][0]} --> {INFO["FILE"][1]}');
      """)
      else:
        file.write(f"""
CREATE TABLE IP_INFO(
  ACTIVE_ID INTEGER PRIMARY KEY,
  ACTIVE_IP TEXT NOT NULL,
  ACTIVE_FILE_DIR TEXT NOT NULL
);

INSERT INTO IP_INFO(ACTIVE_ID,ACTIVE_IP,ACTIVE_FILE_DIR)
VALUES ({id_},'{INFO["IP"][0]}','{INFO["FILE"][0]}');
      """)
    
    crs.execute("SELECT * FROM IP_INFO")
    connect.commit()
    connect.close()
    file.close()
  
    op_and_write = open('database.sql','r').read()
    with open(self.PATH,'w') as file:
      file.write(op_and_write)
      file.close()
