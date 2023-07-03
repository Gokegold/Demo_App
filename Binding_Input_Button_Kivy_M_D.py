"""
Demo_App

Learning Source: https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Function: [Binding_Input_Button_Kivy_M_D.py]

Location: Nigeria

Date Created: JULY 2, 2023

last modification:: [JULY 2, 2023], [JULY 3, 2023]...

from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder

username_helper = """
MDTextField:
    hint_text: "Enter username"
    helper_text: "or click on forgot username"
    helper_text_mode: "on_focus"
    icon_right: "android" 
    icon_color_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    size_hint_x:None
    width:300
"""


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Green"
        # username = MDTextField(text='Enter username',
        #                        pos_hint={'center_x': 0.5,
        #                                  'center_y': 0.5},
        #                        size_hint_x=None, width=300)

        username = Builder.load_string(username_helper)
        screen.add_widget(username)
        return screen


DemoApp().run()
