from kivy.uix.screenmanager import Screen

from py.piechart import PieChart
from kivy.clock import Clock
from functools import partial
from kivy.uix.image import Image


class ProductivityScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chart = Image(source="images/Weekly Success Rate.png")
        Clock.schedule_once(self.add_chart, 1)
        self.chart.size_hint = (1,1)

    def add_chart(self, t):
        self.ids.chart_card.add_widget(self.chart)

