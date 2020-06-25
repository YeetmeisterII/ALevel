from kivy.uix.button import Button


class ToggleEncryptionButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Encrypt'

    def set_text(self, value):
        self.text = value


class PerformButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.text = 'Perform Change'
