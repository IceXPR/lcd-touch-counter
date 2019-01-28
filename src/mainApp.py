import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen


class RootScreen(Screen):
    pass

class MainApp(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(RootScreen())
        return sm

if __name__ == '__main__':
    MainApp().run()