"""
Create Kivy box of three buttons that greet user by input and clear text input and output
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Load the kivy box"""
    def build(self):
        """Build the kivy box"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle the greet button"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Handle the clear button"""
        print("test")
        self.root.ids.output_label.text = ""
        self.root.ids.input_name.text = ""


BoxLayoutDemo().run()
