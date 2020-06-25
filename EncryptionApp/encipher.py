import itertools

from kivy.utils import reify


class Encipher:
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def __init__(self, text: str, key: str, encrypt: bool = True):
        self.original = text
        self.key = key
        self.encrypt = encrypt

    @property
    def convert(self) -> str:
        if not len(self.original):
            return ''
        new_string = self._build_new_string()
        spaced_string = self._split_string(new_string)
        return spaced_string

    @property
    def original(self) -> str:
        return self.__original_text

    @original.setter
    def original(self, value: str) -> None:
        self.__original_text = value.replace(' ', '')

    def _rotate_character(self, character: str, amount: int) -> str:
        if not self.encrypt:
            amount *= -1
        character_pos = self.alpha.index(character.lower())
        rotated_pos = (character_pos + amount) % 26
        rotated_character = self.alpha[rotated_pos]
        return rotated_character

    def _build_new_string(self) -> str:
        get_index = (lambda character: self.alpha.index(character))

        key_map = map(get_index, list(self.key))
        key_list = list(key_map)

        string_map = map(self._rotate_character, list(self.original), itertools.cycle(key_list))
        string_list = list(string_map)
        string = ''.join(string_list)
        return string

    @staticmethod
    def _split_string(string: str) -> str:
        spaces_needed = (len(string) - 1) // 4
        for multiplicand in range(spaces_needed, 0, -1):
            string = string[:4 * multiplicand] + ' ' + string[4 * multiplicand:]
        return string
