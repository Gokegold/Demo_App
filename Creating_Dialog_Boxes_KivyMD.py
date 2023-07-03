"""
Demo_App

Learning Source: https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Function: [Creating Buttons in Material Design _ KivyMD], [Themes_Color_Palettes_Kivy_M_D.py]

Location: Nigeria

Date Created: JULY 3, 2023

last modification::: [JULY 3, 2023]...
"""
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from helpers import username_helper


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.primary_palette = "Blue"
        # username = MDTextField(text='Enter username',
        #                        pos_hint={'center_x': 0.5,
        #                                  'center_y': 0.5},
        #                        size_hint_x=None, width=300)

        button = MDRectangleFlatButton(text='show',
                                       pos_hint={'center_x': 0.5,
                                                 'center_y': 0.4},
                                       on_release=self.show_data)
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
        screen.add_widget(button)
        return screen

    def show_data(self, obj):
        if self.username.text is "":
            check_string = 'Please enter a username'
        else:
            check_string = self.username.text + 'does not exit'
        close_button = MDFlatButton(text='Close',
                                    on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        self.dialog = MDDialog(title='Username Check',
                               text=check_string,
                               size_hint=(0.7, 1),
                               buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()
