#from databaseInterface import databaseConnect
import kivy
import mysql
import mysql.connector
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
from kivy.properties import ObjectProperty
Config.set('graphics', 'resizable', True)
#from mysql.connector import errorcode

class Menu_1(GridLayout):
    def aLittleTeat(self):
      return on_click_connect(usrn, pswd)

class Menu_1App(App):
    def build(self):
        return Menu_1()
    def processUsrn(self):
        text_usrn = self.root.ids.input.text
        usrn = text_usrn
        return usrn
    def processPswd(self):
        text_pswd = self.root.ids.input.text
        pswd = text_pswd
        return pswd

def on_click_connect():
    try:
      cnx = mysql.connector.connect(user=usr, 
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
      return(cnx)

if __name__=='__main__':
    Menu_1App().run()
