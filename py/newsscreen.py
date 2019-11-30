from kivy.uix.screenmanager import Screen
import datetime
from kivy.clock import Clock

class NewsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.move_label, 0)

    def move_label(self, time_passed):
        news_label = self.ids.news_label
        news_label.pos[0] -= time_passed*100
        if news_label.pos[0] < -news_label.width:
            news_label.pos[0] = self.width
