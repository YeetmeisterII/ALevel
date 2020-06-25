class Compress:
    def __init__(self, string):
        self.lines = string.split('\n')
        self.lines_words = []
        self.compressed = ''
        self.reference_list = ['\n']
        self.words = []

    def string_lister(self):
        for line in self.lines:
            words = line.split()
            temp_list = []
            for word in words:
                temp_list.append(word)
                self.reference_list.append(word) if word not in self.reference_list else None
            self.lines_words.append(temp_list)
        print(self.reference_list)
        print()

    def string_replacer(self):
        global working_text
        number_of_digits = 0
        for line in self.lines_words:
            for word in line:
                self.compressed += f'{self.reference_list.index(word)},'
                number_of_digits += 1
            self.compressed += '0,'
            number_of_digits += 1
        self.compressed = self.compressed[:-1]
        # print(self.compressed)
        # print(number_of_digits, len(self.reference_list), number_of_digits * 7, len(working_text) * 8, '\n')
        text = f'{self.reference_list}\n{self.compressed}'
        return text

    def reverter(self):
        uncompressed = ''
        compressed_numbers = self.compressed.split(',')
        compressed_numbers = map(int, compressed_numbers)
        for number in compressed_numbers:
            word = self.reference_list[number]
            uncompressed += f'{word}'
            uncompressed += ' ' if number is not 0 else ''
        uncompressed = uncompressed[:-1]
        print(uncompressed)


f = open('/Users/Germain_Jones/Desktop/madness.txt', 'r', encoding='UTF-8')
working_text = f.read()
f.close()
a = Compress(working_text)
a.string_lister()
n = open('/Users/Germain_Jones/Desktop/compressed.txt', 'w')
n.write(a.string_replacer())
n.close()
# a.reverter()
