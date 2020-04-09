import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
Config.set('graphics', 'resizable', True)

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