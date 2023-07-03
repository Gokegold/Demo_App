"""
File_Name:: Demo_App

Learning Source:: https://www.youtube.com/watch?v=LRXo0juuTrw&list=PLhTjy8cBISEoQQLZ9IBlVlr4WjVoStmy-

Twitter:: @i_amgoke :: https://twitter.com/i_amgoke

Github:: https://www.github.com/Gokegold

Function:: [Creating Buttons in Material Design _ KivyMD], [Themes_Color_Palettes_Kivy_M_D.py]

Location: Nigeria

Date Created:: JULY 3, 2023

last modification:: [JULY 3, 2023]...
"""

username_helper = """
MDTextField:
    hint_text: "Enter Username"
    helper_text: "or click on forgot username"
    # to highlight but make functional when click on
    helper_text_mode: "on_focus"
    icon_right: "android"
    # this is to color the same color as the theme app color
    icon_color_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
    # to adjust the font text size
    size_hint_x:None
    # to adjust the font size of the x axis 
    size:3000
