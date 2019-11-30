from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
from kivymd.app import MDApp
from kivy.utils import get_color_from_hex
from kivymd.color_definitions import colors
from py.homescreen import HomeScreen
from py.newsscreen import NewsScreen
from py.tasksscreen import TasksScreen
from py.productivityscreen import ProductivityScreen
from kivy.uix.screenmanager import FadeTransition
from kivy.core.window import Window

from kivy.uix.vkeyboard import VKeyboard
class KeyboardB(VKeyboard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #super().__init__(pos_hint={"center_x": .5, "center_y": .25}, **kwargs)


Window.set_vkeyboard_class(KeyboardB)

Window.clearcolor = (1,1,1,1)
class MainApp(MDApp):
    def load_screen(self, screen_name):
        self.root.ids.screen_manager.transition = FadeTransition(clearcolor=get_color_from_hex(colors['Light']['Background']))
        self.root.ids.screen_manager.current = screen_name

MainApp().run()
