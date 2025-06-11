
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# جدول التحويل
conversion_table = {
    "fh_": "wlan", "e": "1", "c": "3", "5": "a", "6": "9",
    "8": "7", "f": "0", "b": "4", "a": "5", "0": "f",
    "4": "b", "d": "2", "1": "e", "3": "c"
}

def convert_input(text):
    for k, v in conversion_table.items():
        text = text.replace(k, v)
    return text

class ConverterScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=10, spacing=10, **kwargs)
        self.code_input = TextInput(hint_text="أدخل الكود", multiline=False)
        self.result_label = Label(text="", size_hint_y=2)
        self.convert_button = Button(text="تحويل", on_press=self.convert)
        self.add_widget(self.code_input)
        self.add_widget(self.convert_button)
        self.add_widget(self.result_label)

    def convert(self, instance):
        input_text = self.code_input.text
        result = convert_input(input_text)
        self.result_label.text = result

class SBzyy37App(App):
    def build(self):
        return ConverterScreen()

if __name__ == "__main__":
    SBzyy37App().run()
