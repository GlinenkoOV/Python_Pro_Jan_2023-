import Product
import Customer
import Cart

import sys
from types import ModuleType
if Product not in sys.modules:
    sys.modules['product'] =ModuleType('product')
    code = open('product.py','rb').read()
    exec(code, sys.modules['product'].__dict__)

product = sys.modules['product']
x_1 = Product.Product('banana', 30)
x_2 = Product.Product('apple', 25)
x_3 = Product.Product('orange', 35)
print(x_1)
print(x_2)
print(x_3)


import sys
from types import ModuleType
if Customer not in sys.modules:
    sys.modules['customer'] =ModuleType('customer')
    code = open('customer.py','rb').read()
    exec(code, sys.modules['product'].__dict__)

customer = sys.modules['customer']
customer_1 = Customer.Customer('Ivanov', 'Ivan', '123456789')
customer_2 = Customer.Customer('Ivanov', 'Petro', '123456799')
print(customer_1)
print(customer_2)



import sys
from types import ModuleType
if Cart not in sys.modules:
    sys.modules['cart'] =ModuleType('cart')
    code = open('cart.py','rb').read()
    exec(code, sys.modules['cart'].__dict__)

cart = sys.modules['cart']



