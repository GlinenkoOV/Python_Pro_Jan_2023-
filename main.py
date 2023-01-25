import Product
import Customer
import Cart

x_1 = Product.Product('banana', 30)
x_2 = Product.Product('apple', 25)
x_3 = Product.Product('orange', 35)

customer_1 = Customer.Customer('Ivanov', 'Ivan', '123456789')
customer_2 = Customer.Customer('Ivanov', 'Petro', '123456799')

order_1 = Cart.Cart(customer_1)
order_1.add_product(x_1)
order_1.add_product(x_2, 2)
order_1.add_product(x_3, 35)

print(order_1)

order_2 = Cart.Cart(customer_2)
order_2.add_product(x_2, 10)
print(order_2)




