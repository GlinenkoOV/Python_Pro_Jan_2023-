import Product
import sys
from types import ModuleType
if Product not in sys.modules:
    sys.modules['product'] =ModuleType('product')
    code = open('product.py','rb').read()
    exec(code, sys.modules['product'].__dict__)

product = sys.modules['product']


import Customer

import sys
from types import ModuleType
if Customer not in sys.modules:
    sys.modules['customer'] =ModuleType('customer')
    code = open('customer.py','rb').read()
    exec(code, sys.modules['product'].__dict__)

customer = sys.modules['customer']


class Cart:

    MAX_LIMIT = 40

    def __init__(self, customer: Customer):
        self.customer = customer
        self.__products = []
        self.__quantities = []

    def get_weight(self):
        return sum(self.__quantities)

    def add_product(self, product: Product, quantity: int | float = 1):
        if self.get_weight() + quantity <= Cart.MAX_LIMIT:
            self.__products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        result = 0
        for product, quantity in zip(self.__products, self.__quantities):
            result += product.price * quantity

        return result

    def __str__(self):
        result = f'{self.customer}\n'
        result += '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                      zip(self.__products, self.__quantities)))
        result += f'\nTotal: {self.total()} UAH'
        return result
