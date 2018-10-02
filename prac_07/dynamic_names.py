from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicNames(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = {"Bob Brown", "Lily Lilac", "Barry Blue", "Ruby Red", "Yvonne Yellow"}

    def build(self):
        self.title = "Dynamic Names"
        self.root = Builder.load_file('dynamic_names.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.label_entries.add_widget(temp_label)


DynamicNames().run()