import kivy
from random import random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Ellipse, Rectangle

class MyApp(App):
    title = "Doctor's Assistant Program"
    def build(self):
        root = RootLayout()
        return(root)
class RootLayout():
    pass

if __name__ == '__main__':
    MyApp().run()