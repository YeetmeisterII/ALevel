from kivy.uix.textinput import TextInput
from string import ascii_lowercase


class LowerCaseInput(TextInput):
    _VALID_CHARACTERS = (*ascii_lowercase, ' ')

    def insert_text(self, substring, from_undo=False):
        for character in substring:
            if character.lower() in self._VALID_CHARACTERS:
                super().insert_text(character.lower(), from_undo)


class OutputText(TextInput):
    def set_text(self, value):
        self.text = value
