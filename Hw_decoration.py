# 1_Створіть декоратор, який підраховуватиме, скільки разів
# була викликана декорована функція.
def tags(param,file_name):
    def decorator(func):
        def inner(*args, **kwargs,):
             inner.count += 1
             tmp = func(*args, **kwargs)
             with open(file_name, 'a') as file:
                 file.write(tmp +'\n')
             return f'<{param}>{tmp}<{param}>{inner.count}'
        inner.count = 0
        return inner
    return decorator


@tags('i', 'test.txt')
def get_text():
    return f'Python'

@tags('p', 'test.txt')
def greetings(name):
    return f'Hello, {name}'

print(get_text())
print(get_text())
print(get_text())
print(get_text())
print(get_text.count)

print(greetings('Oleh'))
print(greetings.count)


# 2_Створіть декоратор, який зареєструє декоровану функцію у списку.
my_function = []
def tags(param,file_name):
    def decorator(func):
        def inner(*args, **kwargs,):
             my_function.append(func)
             tmp = func(*args, **kwargs)
             with open(file_name, 'a') as file:
                 file.write(tmp +'\n')
             return f'<{param}>{tmp}<{param}>'
             return func
        return inner
    return decorator


@tags('i', 'test.txt')
def get_text():
    return f'Python'

@tags('p', 'test.txt')
def greetings(name):
    return f'Hello, {name}'

print(get_text())

print(greetings('Oleh'))

# print(my_function)


# 3_Припустимо, у класі визначено метод str. Створіть такий
# декоратор для цього методу,щоб отриманий рядок зберігався у
# текстовий файл. Ім'я файлу має збігатися з ім'ямкласу, в якому
# визначено метод str
def decorator(func):
    def get_str(argument):
        with open(argument.class_name.__name__ + "txt", 'w') as file:
            file.write(func(argument))
    return get_str

class Student:
    def __init__(self, surname, name):
        self.name = name
        self.surname = surname
        self.class_name = self.__class__.__name__


    @decorator
    def __str__(self):
        return f'{self.name} {self.surname} {self.class_name}'


x_1 = Student('Ivanov', 'Ivan')
print(x_1)









