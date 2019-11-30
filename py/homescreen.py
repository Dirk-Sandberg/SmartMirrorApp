from kivy.uix.screenmanager import Screen
import datetime
from kivy.clock import Clock

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.tick, 1)

    def tick(self, time_passed):
        today_date = datetime.date.today()
        today_time = datetime.datetime.now()
        date = today_date.strftime('%b %d, %Y')
        time = today_time.strftime("%H:%M")
        self.ids.date_label.text = date
        self.ids.time_label.text = time

