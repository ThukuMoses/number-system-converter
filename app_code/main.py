from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from Converter import convert_n  # import logic



class ConverterLayout(BoxLayout):

    def safe_convert(self, num, from_base, to_base):
        """
        Wraps convert_n so errors don't crash the app.
        Returns a result string or an error message.
        """
        try:
            return convert_n(num, from_base, to_base)
        except ValueError as e:
            return f"Error: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"

    def convert_number(self, num, from_base, to_base):#calls safe convert to make conversions 
        result = self.safe_convert(num, from_base, to_base)
        self.ids.result_label.text = f"Result: {result}"


class ConverterApp(App):
    def build(self):
        return ConverterLayout()


if __name__ == "__main__":
    ConverterApp().run()
