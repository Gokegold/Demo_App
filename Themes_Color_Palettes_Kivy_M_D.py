"""
Demo_App

Learning Source: https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

Twitter @i_amgoke: https://twitter.com/i_amgoke

Github: https://www.github.com/Gokegold

Function: [Creating Buttons in Material Design _ KivyMD], [Themes_Color_Palettes_Kivy_M_D.py]

Location: Nigeria

Date Created: JULY 2, 2023

last modification:: [JULY 2, 2023], 

"""
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDFlatButton, MDRectangleFlatButton, MDIconButton, MDFloatingActionButton
from kivymd.uix.screen import Screen


class DemoApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Yellow"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Dark"
        screen = Screen()
        username = MDTextField(text='Enter username',
                               pos_hint={'center_x': 0.5, 'center_y': 0.5},
                               size_hint_x=None, width=300)
        screen.app_widget(username)
        btn_flat = MDRectangleFlatButton(text='Hello World!',
                                         pos_hint={'center_x': 0.5,
                                                   'center_y': 0.5})
        icon_btn = MDFloatingActionButton(icon='language-python',
                                          pos_hint={'center_x': 0.5,
                                                    'center_y': 0.5})
        # screen.add_widget(btn_flat)

        label = MDLabel(text='Hello World !',
                        halign='center',
                        theme_text_color='Custom',
                        text_color=(236 / 225.0, 98 / 225.0, 1 / 225.0),
                        font_style='Caption')

        icon_label = MDFloatingActionButton(icon='language-python', halign='center')
        return screen


DemoApp().run()
