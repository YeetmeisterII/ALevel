from math import ceil

import numpy as np
from PIL import Image


class ImageProducer:

    def __init__(self, string: str):
        self._string = string
        self._image_array = self._create_image_array()

    def __call__(self):
        return self.create_image()

    @property
    def _columns(self):
        return len(self._image_array)

    @property
    def _rows(self):
        return len(self._image_array[0])

    def _create_image_array(self):
        str_length = len(self._string)
        image_length = int(ceil(str_length ** 0.5))
        values = [ord(char) for char in self._string] + [0] * (image_length ** 2 - str_length)
        return np.array(values).reshape(image_length, image_length)

    def _put_pixels(self, image: Image):
        for row in range(self._rows):
            for column in range(self._columns):
                print(self._image_array[row][column])
                value = tuple([self._image_array[row][column]] * 3)
                image.putpixel((column,row), value)

    def create_image(self):
        image = Image.new("RGB", (self._columns, self._rows))
        self._put_pixels(image)
        return image
