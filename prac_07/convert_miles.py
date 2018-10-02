from kivy.app import App
from kivy.lang import Builder


class ConvertMiles(App):
    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_miles.kv')
        return self.root

    def handle_increment(self, increment):
        value = self.check_miles() + increment
        self.root.ids.input_number.text = str(value)
        self.handle_calculation()

    def check_miles(self):
        try:
            value = int(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

    def handle_calculation(self):
        value = self.check_miles()
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)


ConvertMiles().run()
