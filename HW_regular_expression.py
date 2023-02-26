# 1_Напишіть регулярний вираз, який знаходитиме в тексті фрагменти,
# що складаються з однієї літери R, за якою слідує одна або більше літер b, за якою одна r.
# Враховувати верхній та нижній регістр.
import re
string = input('input string:' )
pattern =r'[R]b*[r]'
result = re.search(pattern, string)
print(result)

# 2_Напишіть функцію, яка виконує валідацію номера банківської картки (9999-9999-9999-9999).
import re
string = '9999-9999-9999-9999'
pattern = r'\d{4}-\d{4}-\d{4}-\d{4}'
match = re.search(pattern, string)
if match:
 print(match.group())
else:
 print("pattern not found")

# 4 Напишіть функцію, яка перевіряє правильність логіну. Правильний логін – рядок від 2 до 10 символів, що містить
# лише літери та цифри.
import re
def func(seq):
    pattern = r'\d{2,10}\D'
    result = re.search(pattern, seq)
    if result:
        print(result)
    else:
        print("seq not correct")

x = func('12R3454444r5')