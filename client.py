#from databaseInterface import databaseConnect
from tkinter import *
import mysql
from mysql.connector import errorcode

window = Tk()

window.title("Doctor's Assistant Client")

window.geometry('350x200')
usrnlbl = Label(window, text="Hello")
usrnlbl.grid(column=0, row=1)
usrn = Entry(window,width=25)
usrn.grid(column=0, row=0)

pswdlbl = Label(window, text="Hello")
pswdlbl.grid(column=0, row=2)
pswd = Entry(window,width=25)
pswd.grid(column=0, row=3)

hostlbl = Label(window, text="Hello")
hostlbl.grid(column=0, row=5)
host = Entry(window,width=25)
host.grid(column=0, row=6)

def on_click_connect():
    cursor = "hi"# databaseConnect.open_connection(usrn.get(), pswd.get(), host.get())
    return cursor

cxtbt = Button(window, text="Connect", command=on_click_connect)
cxtbt.grid(column=2, row=0)

window.mainloop()

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
print(db.execute("show databases;"))