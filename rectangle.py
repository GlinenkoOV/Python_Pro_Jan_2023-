import numbers


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __volume(self):
        return self.x * self.y

    def __lt__(self, other):
        return self.__volume() < other.__volume()

    def __le__(self, other):
        return self.__volume() <= other.__volume()

    def __gt__(self, other):
        return self.__volume() > other.__volume()

    def __ge__(self, other):
        return self.__volume() >= other.__volume()

    def __eq__(self, other):
        return self.__volume() == other.__volume()

    def __ne__(self, other):
        return self.__volume() != other.__volume()

    def __add__(self, other):
        return self.__volume() + other.__volume

    def __str__(self):
        return f'{self.x} {self.y}'

    def __add__(self, other):
        return Rectangle(self.x+other.x, self.y+other.y)

    def __mul__(self, other):
        if isinstance(other, numbers.Real):
            return Rectangle(self.x * other, self.y * other)
        else:
            return NotImplemented


    def __str__(self):
        return f'x = {self.x} , y =  {self.y}'

rectangle_1 = Rectangle(2, 3)
rectangle_2 = Rectangle(6, 2)
print(rectangle_1 > rectangle_2)
print(rectangle_1 <= rectangle_2)
print(rectangle_1 >= rectangle_2)
print(rectangle_1 != rectangle_2)
print(rectangle_1 == rectangle_2)

rectangle_3 = rectangle_1 + rectangle_2
print(rectangle_3)

rectangle_4 = rectangle_2 * 2

print(rectangle_4)
