from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class ConverterApp(App):
    def build(self):
        layout = BoxLayout(orientation="horizontal")

        self.input = TextInput(hint_text="Enter a decimal number")
        layout.add_widget(self.input)

        self.result = Label(text="Result will appear here")
        layout.add_widget(self.result)

        btn = Button(text="Convert to Binary")
        btn.bind(on_press=self.convert_to_binary)
        layout.add_widget(btn)

        return layout

    def convert_to_binary(self, instance):
        try:
            number = int(self.input.text)
            self.result.text = bin(number)[2:]  # decimal → binary
        except:
            self.result.text = "Invalid input!"

if __name__ == "__main__":
    ConverterApp().run()
