class Product:

    def __init__(self, title: str, price: int | float):
        self.title = title
        self.price = price

    def __str__(self):
        return f'{self.title}: {self.price} UAH'
class CartIterator:
    def __init__(self, products):
        self.__products = products
        self.index = 0

    def __next__(self):
        if self.index < len(self.__products):
            self.index = self.index + 1
            return self.__products[self.index - 1]
        raise StopIteration()

    def __iter__(self):
        return self


class Customer:

    def __init__(self, surname, name, phone):
        self.surname = surname
        self.name = name
        self.phone = phone

    def __str__(self):
        return f'{self.surname} {self.name[0]}.; {self.phone}'

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
    def __iter__(self):
         return CartIterator(self.__products)


x_1 = Product('banana', 30)
x_2 = Product('apple', 25)
x_3 = Product('orange', 35)

customer_1 = Customer('Ivanov', 'Ivan', '123456789')
customer_2 = Customer('Ivanov', 'Petro', '123456799')

order_1 = Cart(customer_1)
order_1.add_product(x_1)
order_1.add_product(x_2, 2)
order_1.add_product(x_3, 35)

# print(order_1)

order_2 = Cart(customer_2)
order_2.add_product(x_2, 10)
# print(order_2)

for product in order_1:
     print('Order_1:', product)


for product in order_2:
    print('Order_2', product)
