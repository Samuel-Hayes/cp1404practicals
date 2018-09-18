from kivy.app import App
from kivy.lang import Builder


class ConvertMiles(App):
    def build(self):
        self.title = "Convert miles to kilometres"
        self.root = Builder.load_file('convert_miles.kv')
        return self.root

    def handle_up(self, value):
        if value.text == '':
            value.text = '0'
        value += 1
        self.root.ids.input_number.text = str(value)

    def handle_down(self, value):
        if value.text == '':
            value.text = '0'
        value -= 1
        self.root.ids.input_number.text = str(value)

    def handle_convert(self, value):
        if value.text == '':
            value.text = '0'
        result = value * 1.60934
        self.root.ids.output_label.text = str(result)
ConvertMiles().run()
