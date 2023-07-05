from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList, OneLineListItem

from helpers import username_helper


class DemoApp(MDApp):

    def build(self):
        screen = Screen()
        list_view = MDList()

        self.theme_cls.primary_palette = "Blue"
        # username = MDTextField(text='Enter username',
        #                        pos_hint={'center_x': 0.5,
        #                                  'center_y': 0.5},
        #                        size_hint_x=None, width=300)

        button = MDRectangleFlatButton(text='show',
                                       pos_hint={'center_x': 0.5,
                                                 'center_y': 0.4},
                                       on_release=self.show_data)
        screen.add_widget(button)
        # Below the username method has been created with its
        # Properties of values imported into it.
        self.username = Builder.load_string(username_helper)
        screen.add_widget(self.username)
      
        item1 = OneLineListItem(text='Item 1')
        item2 = OneLineListItem(text='Item 2')
        list_view.add_widget(item1)
        list_view.add_widget(item2)
        screen.add_widget(list_view)

        return screen

    def show_data(self, obj):
        # If the username field is left blank
        # Then a string will be passed 'Please enter a username
        if self.username.text is " ":
            check_string = ' Please enter a username '
        else:
            # else if the username is wrong then enter 'does not exit'

            check_string = self.username.text + 'does not exit'
            # below we create an instance(method) for the closed button
            # that what we want the close but to do.
        close_button = MDFlatButton(text='Close',
                                    # The on_release function below gives it
                                    # The access closes when the button
                                    # is clicked on.
                                    on_release=self.close_dialog)
        more_button = MDFlatButton(text='More')
        # below recall the
        self.dialog = MDDialog(title='Username Check',
                               text=check_string,
                               # The below shows how much
                               # We would want the dialog box to occupy
                               # So for half the screen size we use 0.5
                               # That is 50% of the screen space.
                               # that is multiplying 0.5 * 100
                               # With this it can work on any mobile or ipad
                               # but using 0.7 makes it better
                               # find what makes it better
                               size_hint=(0.7, 1),
                               # This is for adding a button to the dialog Box
                               # Here added the button as a list
                               buttons=[close_button, more_button])
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


DemoApp().run()
