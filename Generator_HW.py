#1_Реалізуйте генераторну функцію, яка повертатиме по одному члену геометричної прогресії із зазначеним множником.
def geometric(start, stop, step):
    while start <= stop:
        yield start
        start *= step

x = geometric(5,20,2)
print(next(x))
for item in x:
    print(item)

#3_Напишіть функцію-генератор, яка повертатиме прості числа. Верхня межа діапазону повинна бути задана параметром цієї функції.
def prime_number(start, stop, step):
    i = 2
    while start <= stop:
        if start % i:
            yield start
            start += step

x = prime_number(2, 40, 1)
print(next)
for item in x:
    print(item)



#4_Напишіть генераторний вираз для заповнення списку. Список повинен бути заповнений кубами чисел від 2  до вказаної вами величини.

a = [x ** 3 for x in range(2, 10)]
print(a)




