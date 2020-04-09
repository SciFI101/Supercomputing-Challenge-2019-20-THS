#from databaseInterface import databaseConnect
#import mysql
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)
#from mysql.connector import errorcode

class Menu_1(GridLayout):
    pass
class Menu_1App(App):
    def build(self):
        return Menu_1()
    def process(self):
        text = self.root.ids.input.text
        print(text)

if __name__=='__main__':
    Menu_1App().run()

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