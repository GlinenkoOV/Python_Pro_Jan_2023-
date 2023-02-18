# 7. Створіть ABC клас із абстрактним методом перевірки цілого числа на простоту. Тобто якщо
# параметром цього методу є ціле число і воно просте, то метод повинен повернути True,
# а в іншому випадку False. Створіть похідний клас. Перевірте працездатність проекту.

from abc import ABC, abstractmethod

class Verification(ABC):
    @abstractmethod
    def validate(self, number):
        'Validate number'

class NumberValidator(Verification):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f'{self.number}'

    def validate(self, number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

validator_1 = NumberValidator(4)
print(validator_1)
