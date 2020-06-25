from kivy.event import EventDispatcher

from EncryptionApp.encipher import Encipher


class EncryptionEvents(EventDispatcher):
    encrypt = True

    def toggle_encrypt(self, toggle_button):
        self.encrypt = not self.encrypt
        toggle_button.set_text('Encrypt') if self.encrypt else toggle_button.set_text('Decrypt')

    def convert_text(self, text, key):
        return Encipher(text, key, self.encrypt).convert
