from kivy.uix.screenmanager import Screen
import datetime
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.toast import toast
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.core.window import Window

class ContentForAnimCard(BoxLayout):
    callback = ObjectProperty(lambda x: None)
    #def resize(self, *args):
    #    self.parent.parent.check_open_box(self)

from kivymd.uix.dialog import MDInputDialog
class TasksScreen(Screen):
    callback = ObjectProperty(lambda x: None)
    task_description = ""
    task_name = ""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.create_dones, 1)
        Clock.schedule_once(self.create_todos, 1)

    def new_task(self):
        a = MDInputDialog(title="Task Name", size_hint=(.5, .5), pos_hint={"center_x": .5, "center_y": .5},
                          events_callback = self.on_task_name, text_button_ok="Next")
        a.open()


    def on_task_name(self, option, dialog):
        self.task_name = dialog.text_field.text
        a = MDInputDialog(title="Task Description", size_hint=(.5, .5), pos_hint={"center_x": .5, "center_y": .5},
                          events_callback = self.on_task_description, text_button_ok="Add Task")
        a.open()


    def _keyboard_close(self, *args):
        pass

    def on_task_description(self, option, dialog):
        self.task_description = dialog.text_field.text

        content = ContentForAnimCard(callback=self.callback)
        content.ids.label.text = self.task_description
        today_date = datetime.date.today()
        date = today_date.strftime('%m/%d/%y')

        exp_panel = MDExpansionPanel(content=content,
                                     icon='images/unchecked_box.png',
                                     title=self.task_name,
                                     secondary_text="Started " + date)
        self.ids.todo_list.add_widget(exp_panel, len(self.ids.todo_list.children))

    def remove_item(self, item):
        todo_list = self.ids.todo_list
        done_list = self.ids.done_list
        if item in todo_list.children:
            todo_list.remove_widget(item)
        elif item in done_list.children:
            done_list.remove_widget(item)

    def move_todo_to_done(self, item):
        todo_list = self.ids.todo_list
        done_list = self.ids.done_list

        today_date = datetime.date.today()
        date = today_date.strftime('%m/%d/%y')
        item.secondary_text = "Finished " + date
        item.icon = 'images/checked_box.png'
        item.content.is_completed = True

        todo_list.remove_widget(item)
        done_list.add_widget(item, len(done_list.children))

    def create_todos(self, *args):
        names_contacts = (
            'Laundry', 'Study for SEIS 610', 'Call Patrick', 'Meal Prep', 'Preorder Cybertruck', 'Handle Business')
        dates = ('11/01/19', '11/10/19', '11/21/19', '11/22/19', '11/27/19', '11/30/19')
        for i,name_contact in enumerate(names_contacts):
            content = ContentForAnimCard(callback=self.callback)
            exp_panel = MDExpansionPanel(content=content,
                             icon='images/unchecked_box.png',
                             title=name_contact, secondary_text="Started " + dates[i])
            self.ids.todo_list.add_widget(exp_panel)



    def create_dones(self, *args):
        names_contacts = (
            'Meeting with Robert', 'Project Due')
        dates = ('11/01/19', '11/10/19')
        for i, name_contact in enumerate(names_contacts):
            content = ContentForAnimCard(callback=self.callback)
            exp_panel = MDExpansionPanel(content=content,
                             icon='images/checked_box.png',
                             title=name_contact, secondary_text="Finished " + dates[i])
            exp_panel.content.is_completed = True
            self.ids.done_list.add_widget(exp_panel)


    #def callback(self, text):
    #    toast(f'{text} to {self.content.name_item}')

