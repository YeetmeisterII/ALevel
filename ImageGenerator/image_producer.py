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
    def _x(self):
        return len(self._image_array)

    @property
    def _y(self):
        return len(self._image_array[0])

    def _create_image_array(self):
        str_length = len(self._string)
        image_length = int(ceil(str_length ** 0.5))
        values = [ord(char) for char in self._string] + [0] * (image_length ** 2 - str_length)
        x1 = np.full((image_length, 1, 3), 255)
        x2 = np.array(values).reshape(image_length, image_length)
        x3 = np.multiply(x2, x1)
        return x3

    def _put_pixels(self, image: Image):
        for x in range(self._x):
            for y in range(self._y):
                print(self._image_array[x][y])
                image.putpixel((x, y), self._image_array[x][y])

    def create_image(self):
        image = Image.new("RGB", (self._x, self._y))
        self._put_pixels(image)
        return image


if __name__ == '__main__':
    string = "test"
    im_producer = ImageProducer(string)
    im = im_producer.create_image()
    im.save("generated_image.png")
