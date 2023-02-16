# 4. Створіть дескриптор, який робитиме поля доступними лише для читання
class MyDescriptor:
    def __init__(self, text):
        self.text = text

    def __get__(self, instance_self, instance_class):
        return self.text + instance_self.name + instance_self.surname

    def __set__(self, instance_self, value):
        raise AttributeError("field is read-only")

class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'{self.surname} {self.name[0]}'

    students = MyDescriptor("Hello  Dear, ")

x_1 = Student('Ivan ', "Ivanov")
print(x_1.students)
# x_1.students ='world'
# print(x_1.students)


# 5. Реалізуйте функціонал, який заборонятиме встановлення полів класу будь-якими значеннями, крім цілих чисел.

class MyDescriptor:
     def __init__(self, value):
        self.value = value
     def __get__(self, instance_self, instance_class):
         return self.value * instance_self.p

     def __set__(self, instance_self, value):
         if self.value != int:
            raise ValueError("Only integers are allowed")
         else:
             self.value = value

class Box:
    def __init__(self, x, y, z):
         self.p = x*y*z
    volume = MyDescriptor(2)

box_1 = Box(1, 2, 3)
print(box_1.volume)
box_1.volume = "Hello"
print(box_1.volume)

box_1.volume = 3
print(box_1.volume)



# 6. Реалізуйте властивість класу, яка має наступний функціонал: при установці значення цієї властивості у файл із
# заздалегідь визначеним ім'ям повинен зберігатися час (коли встановлювали значення властивості)
# та встановлене значення.
import time
class MyDescriptor:
    def __init__(self, value):
        self.value = value

    def __get__(self, instance_self, instance_class):
        return self.value * instance_self.p

    def __set__(self, instance_self, value):
        self.value = value
        with open('test.txt','w') as file:
            time_s= time.localtime()
            file.write(f'{time_s} , Value = {self.value}')


class Box:
    def __init__(self, x, y, z):
        self.p = x * y * z

    volume = MyDescriptor(2)


box_1 = Box(1, 2, 3)
print(box_1.volume)

box_1.volume = 3
print(box_1.volume)