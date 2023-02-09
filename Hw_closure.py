# 1_ 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається за допомогою функції користувача.
#  Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, що видаються послідовностю.
#  Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
def pow_2(item):
    return item ** 2

def gen_items(start, stop, step, func):
    while start < stop:
        yield func(start)
        start += step

for item in gen_items(1, 11, 1, pow_2):
    print(item)

#2_Використовуйте отриманий механізм для прискорення функції рекурсивного обчислення n - го члена ряду Фібоначчі(метод мемоїзації)
# Порівняйте швидкість виконання із просто рекурсивним підходом.
import timeit
import functools

stmt_closure = """
def fibonacci():
    res = [0, 1]

    def get_value(n):
        if len(res) > n:
            return res[n]

        prev, cur = res[-2], res[-1]
        while len(res) <= n:
            prev, cur = cur, cur + prev
            res.append(cur)
        return res[-1]

    return get_value
f = fibonacci()
f(40)
"""


stmt_recursion = """
import functools
@functools.lru_cache
def recursion_fibonacci(n):
    if n <= 1:
        return n
    return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)
recursion_fibonacci(40)
"""


print(timeit.timeit(stmt_closure, number=10))
print(timeit.timeit(stmt_recursion, number=10))


# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.
def seq_modifier(seq, func):
    return sum(func(item) for item in seq)
x =[1, 2, 3, 4, 5, 6, 7 ]
print(seq_modifier(x, lambda item: item ** 2))
print(seq_modifier(x, lambda item: item ** 3))
print(seq_modifier(x, lambda item: item))








