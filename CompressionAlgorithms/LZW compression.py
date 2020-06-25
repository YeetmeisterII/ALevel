class LZW:
    def __init__(self, uncompressed_string):
        self.uncompressed_string = uncompressed_string
        self.characters_lookup, self.characters, = self.get_character_set(self.uncompressed_string)
        self.compressed_string = self.compressor()

    @staticmethod
    def get_character_set(uncompressed):
        characters_cleaned = sorted(list(set(uncompressed)))
        characters_cleaned_dict = {}
        for character in characters_cleaned:
            characters_cleaned_dict.update({character: [character]})
        return characters_cleaned_dict, characters_cleaned

    def compressor(self):
        characters_lookup = self.characters_lookup
        characters = list.copy(self.characters)
        compressed_string = []
        part_a = self.uncompressed_string[0]
        for character in self.uncompressed_string[1:]:
            part_c = part_a + character
            first_character = part_c[0]
            if part_c not in characters_lookup[first_character]:
                characters_lookup[first_character].append(part_c)
                characters.append(part_c)
                compressed_string.append(characters.index(part_a))
                part_a = character
            else:
                part_a = part_c
        return compressed_string

    def decompressor(self, compressed_string):
        characters = list.copy(self.characters)
        string = ''
        part_a = compressed_string[0]
        letter_a = characters[part_a]
        string += letter_a
        characters.append(letter_a)
        for index in compressed_string[1:]:
            letter_b = characters[index]
            characters[-1] += letter_b
            characters.append(letter_b)
            string += letter_b
        return string
