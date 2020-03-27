from databaseInterface import databaseConnect
from tkinter import *

window = Tk()

window.title("Doctor's Assistant Client")


usrn = Entry(window,width=10)
pswd = Entry(window,width=10)
host = Entry(window,width=10)

def on_click_connect():
    cursor = databaseConnect.open_connection(usrn.get(), pswd.get(), host.get())
    return cursor

window.mainloop()