import argparse
import logging
from argparse import ArgumentParser

logging.basicConfig(filename='rectangle.log',
                    filemode='a',
                    encoding='utf-8',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class NegativeValueError(ValueError):
    pass


class Rectangle:
    def __init__(self, width, height=None):
        try:
            if width <= 0:
                logging.info(f'Получена ширина: {width}')
                raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
            self._width = width
            logging.info(f'Получена ширина: {self._width}')
            if height is None:
                self._height = width
                logging.info(f'Получены ширина и высота:{self._height}')
            else:
                if height <= 0:
                    logging.info(f'Получена высота :{height}')
                    raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
                self._height = height
                logging.info(f'Получена высота :{self._height}')

        except NegativeValueError as e:
            logging.error(e)


    def perimeter(self):
        res = 2 * (self._width + self._height)
        logging.info(f'Периметр треугольника с шириной {self._width} и высотой {self._height} составляет {res}')
        return res


    def area(self):
        res = self._width * self._height
        logging.info(f'Площадь треугольника с шириной {self._width} и высотой {self._height} составляет {res}')
        return res

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

rect1 = Rectangle(5, 10)
rect2 = Rectangle(-3, -5)
print(f"Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect1: {rect1.area()}")



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rectangle Operations')
    parser.add_argument('--width', metavar='width', type=int, help='Width of the rectangle', required=True)
    parser.add_argument('--height', metavar='height',  type=int, help='Height of the rectangle')
    args = parser.parse_args()

    width = args.width
    height = args.height
    rectangle = Rectangle(width, height)
    print('Perimeter:', rectangle.perimeter())
    print('Area:', rectangle.area())
