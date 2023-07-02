"""
Demo_App

Learning Source: https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Location: Nigeria

Date Created: JULY 2, 2023

last modification:: [JULY 2, 2023], 

"""

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

username_helper = """
MDTextField:
    hint_text: "Enter username"
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        # username = MDTextField(text='Enter username',
        #                        pos_hint={'center_x': 0.5,
        #                                  'center_y': 0.5},
        #                        size_hint_x=None, width=300)

        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen


DemoApp().run()
