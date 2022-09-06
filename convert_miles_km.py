from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesKmDemo(App):
    km_shows = StringProperty()

    def build(self):
        self.title = "Convert Miles Km Demo"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment):
        mile = self.get_valid_input()
        mile += increment
        self.root.ids.input_mile.text = str(mile)

    def handle_calculation(self):
        mile = self.get_valid_input()
        km = str(mile * MILES_TO_KM)
        self.km_shows = km

    def get_valid_input(self):
        try:
            result = float(self.root.ids.input_mile.text)
            return result
        except ValueError:
            return 0


ConvertMilesKmDemo().run()
