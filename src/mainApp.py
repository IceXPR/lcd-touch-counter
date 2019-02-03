import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.config import Config

import RPi.GPIO as GPIO

counter = 0  # Hardware counter, keeps count of times buttons pushed

    
class RootScreen(Screen):
    """ Create main screens """
    visual_counter = StringProperty('0')  # Counter numeric display property

class MainApp(App):
    """ Main application code to launch screen display """
    sm = ScreenManager()  # Creates a maanger for the screen
    Window.fullscreen = 'auto'
    Config.set('graphics', 'fullscreen', 'auto')
    Config.set('graphics', 'window_state', 'maximize')
    Config.write()  # Writes the full screen configuration

    def button_callback(self, channel):
        """ This is the action when the hardware button is pressed """
        global counter
        counter = counter + 1  # increase the counter by one
        print("Button was pushed!" + str(counter))  # display the output on console
        self.sm.get_screen('rootscreen').visual_counter = str(counter)  # updates the display counter using the hardware counter

    def build(self):
        """ Builds the window and wire the button """
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)  # set the pins on the board
        GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # set the pin 10 on the board
        GPIO.add_event_detect(10,GPIO.RISING,callback=self.button_callback, bouncetime=200)  # wire pin 10 to the action callback function above
        
        self.sm.add_widget(RootScreen())  # adds the display to the screen manager
        return self.sm
    
    def on_request_close(self):
        """ When app is closed cleanup the GPIO on the Raspberry """
        GPIO.cleanup()
        print("Cleaned up completed...")

if __name__ == '__main__':
    MainApp().run()