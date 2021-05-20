# 2 - Creating Buttons and Triggering Events
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Phone No.: "))
        self.ph_no = TextInput(multiline=False)
        self.inside.add_widget(self.ph_no)

        self.inside.add_widget(Label(text="Email ID: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        ph_no = self.ph_no.text
        email = self.email.text

        print("Name: {n}\nPhone No.: {p}\nEmail: {e}".format(n=name, p=ph_no, e=email))
        self.name.text = ""
        self.ph_no.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
