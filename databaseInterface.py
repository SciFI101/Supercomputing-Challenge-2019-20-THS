
#Python 3.6.5
import mysql
from mysql.connector import errorcode



class databaseConnect:
  def __init__(self):
    self.cur = ''
    self.cnx = ''
  def open_connection(self, usr, pwd, hostip):
    try:
      self.cnx = mysql.connector.connect(user=usr, 
                                    password=pwd,
                                    host=hostip)
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      print('We\'re in bois')
      return(self.cur)

db = databaseConnect.open_connection("root", "artemisfowl", "localhost" )
db.execute("show databases;")