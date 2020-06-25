import kivy
from kivy.lang import Builder

kivy.require('1.11.1')

from kivy.config import Config

Config.set('input', 'mouse', 'mouse,multitouch_on_demand')

from kivy.metrics import dp
from kivy.core.window import Window

Window.size = (dp(400), dp(200))

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

from EncryptionApp.event_handler import EncryptionEvents


class EncryptionScreen(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.event_controller = EncryptionEvents()
        self.toggle_button.bind(on_press=self.event_controller.toggle_encrypt)
        self.perform_button.bind(on_press=self.update_output_box)
        self.output_box.bind()

    def update_output_box(self, *args):
        conversion = self.event_controller.convert_text(self.input_box.text, self.key_box.text)
        self.output_box.set_text(conversion)


class EncryptionApp(App):
    def build(self):
        screen = EncryptionScreen()
        return screen


def main():
    EncryptionApp().run()


if __name__ == '__main__':
    main()
