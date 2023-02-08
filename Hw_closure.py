# 1_ 1. Реалізуйте генераторну функцію, яка повертатиме по одному члену числової послідовності, закон якої задається за допомогою функції користувача.
#  Крім цього параметром генераторної функції повинні бути значення першого члена прогресії та кількість членів, що видаються послідовностю.
#  Генератор повинен зупинити свою роботу або по досягненню n-го члена, або при передачі команди на завершення.
def gen_func(first, n):
    def get_next():
        nonlocal first
    for i in range(n):
        yield first
        first += 1
    return get_next()

for i in gen_func(1,10):
    print(i)
# 3. Напишіть функцію, яка застосує до списку чисел довільну функцію користувача і поверне суми елементів отриманого списку.
def my_list(list, get_sum):
 result = []
 for i in list:
    if get_sum(i) == True:
        result.append(i)
 return result

list = [1, 2, 3, 4, 5]

def get_sum(num):
 if num >= 0:
    return True
 else:
    return False
a = my_list(list, get_sum)
print((a))
print(sum(a))