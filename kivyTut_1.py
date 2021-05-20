# 1 - Label, Input and GUI Layouts
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Phone No.: "))
        self.ph_no = TextInput(multiline=False)
        self.add_widget(self.ph_no)

        self.add_widget(Label(text="Email ID: "))
        self.email = TextInput(multiline=False)
        self.add_widget(self.email)


class MyoneApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyoneApp().run()
