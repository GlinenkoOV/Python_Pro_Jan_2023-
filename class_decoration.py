#1. Створіть декоратор, який зареєструє декорований клас у списку.
def decorator(cls):
    list = []
    def add_list(*args, **kwargs):
        tmp = cls(*args, **kwargs)
        list.append(cls)
        return tmp
    return add_list

@decorator
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}'

x_1 = Student('Ivan', "Ivanov")
print (x_1)
print(list)



#3. Для класу Box напишіть статичний метод, який підраховуватиме сумарний обсяг двох ящиків, які будуть його параметрами.

class Box:
     def __init__(self, x, y, z):
         self.x = x
         self.y = y
         self.z = z

     def __str__(self):
        return f'{self.x} {self.y } {self.z} '

     def volume(self):
        return self.x * self.y * self.z

     @staticmethod
     def get_boxes(box_1, box_2):
        return (box_1.volume() + box_2.volume())

box_1 = Box(1, 2, 3)
box_2 = Box(1, 2, 4)

print(Box.get_boxes(box_1, box_2))

#2. Створіть клас декоратора з параметром. Параметром має бути рядок, який повинен дописуватись (ліворуч) до результату роботи методу str.
def Parametr(param):
    def decoration(cls):
        def inner(*args, **kwargs):
        tmp = cls(*args, **kwargs)
        return f'{param} + {tmp}'
        return inner
    return decoration


@Parametr("Hello")
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.name} {self.surname}'

x_1 = Student('Ivanov', 'Ivan')
print(x_1)



