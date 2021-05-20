# 3 - kv Designing Language
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    name_py = ObjectProperty(None)
    email_py = ObjectProperty(None)

    def btn(self):
        print("Name: {n}\nEmail: {e}".format(n=self.name_py.text, e=self.email_py.text))
        self.name_py.text = ""
        self.email_py.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
