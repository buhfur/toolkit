#!/usr/bin/env python3
#user interface for the toolkit 
from textual.app import App


class NewApp(App):

    #event handler that plays a beep when the 
    def on_key(self):
        self.console.bell()



NewApp.run() 
