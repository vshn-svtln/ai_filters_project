import math
from PIL import Image


class Filter:
    """
    Базовый класс для создания фильтров.
    """

    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # Этот метод нужно будет реализовать в новых классах.
        raise NotImplementedError

    def apply_to_image(self, img: Image.Image) -> Image.Image:
        # цикл по всем пикселям
        # img.width - ширина картинки
        # img.height - высота картинки
        for i in range(img.width):
            for j in range(img.height):
                # получаем цвет
                r, g, b = img.getpixel((i, j))

                # как-либо меняем цвет
                new_colors = self.apply_to_pixel(r, g, b)

                # сохраняем пиксель обратно
                img.putpixel((i, j), new_colors)
        return img


class RedFilter(Filter):
    def apply_to_pixel(self, r: int, g: int, b: int) -> tuple[int, int, int]:
        # плавно усиляет красный
        r = int(math.exp(r / 255) / math.e * 255)
        return r, g, b



#Саша
class LighteninGeer():

    def __init__(self, x, y, pic):
        self.x = x
        self.y = y
        self.pic = pic

    def  lightening(self):
        for i in range(self.x):
            for j in range(self.y):
                value = self.pic.getpixel((i, j))
                if value < 200:
                    new_value = value + 50
                    self.pic.putpixel((i, j), new_value)

        return self.pic.show()