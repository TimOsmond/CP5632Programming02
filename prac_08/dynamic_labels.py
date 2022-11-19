"""
Dynamic list of names as labels.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicLabelsApp(App):
    """Create dynamic labels."""
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.collection_of_names = {"George", "Fred", "John", "Tim"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):
        """Create labels from dictionary entries and add them to the GUI."""
        for name in self.collection_of_names:
            temp_label = Label(text=name)
            temp_label.bind()
            self.root.ids.main.add_widget(temp_label)

    def print(self, instance):
        """Access names from dict."""
        name = instance.text
        self.status_text = f"{name}"


DynamicLabelsApp().run()
