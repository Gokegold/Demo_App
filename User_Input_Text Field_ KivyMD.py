"""
Demo_App

Learning Source: https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Function: [Creating Buttons in Material Design _ KivyMD], [Themes_Color_Palettes_Kivy_M_D.py]

Location: Nigeria

Date Created: JULY 2, 2023

last modification:: [JULY 2, 2023], [JULY 2, 2023]...
"""
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.textfield import MDTextField
from kivy.lang import Builder
from helpers import username_helper


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Blue"
        # username = MDTextField(text='Enter username',
        #                        pos_hint={'center_x': 0.5,
        #                                  'center_y': 0.5},
        #                        size_hint_x=None, width=300)
        # creating button instance
        button = MDRectangleFlatButton(text='show',
                                       pos_hint={'center_x': 0.5,
                                                 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

        # to show the entered text.
    def show_data(self, obj):
        print(self.username.text)



DemoApp().run()
