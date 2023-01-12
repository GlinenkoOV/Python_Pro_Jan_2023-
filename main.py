class Goods:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        print(f"Product description: {self.price} UAH,{self.description},{self.dimensions} g")


    def __str__(self):
        return f'{self.price} {self.description} {self.dimensions}'


class Buyer:
    def __init__(self, name, city, phone):
        self.name = name
        self.city = city
        self.phone = phone

        print(f"Buyer description:{self.name}, {self.city},{self.phone}")

        def __str__(self):
            return f'{self.name} {self.city} {self.phone}.'


class Order:
    def __init__(self, title):
        self.title = title
        self.orders = []

    def add_orders(self, order: Goods):
            self.orders.append(order)


    def sum_orders(self):
        total = 0
        for element in self.orders:
            total += element
        return total
        print(sum_orders)

    def __str__(self):
        return f'{self.title}\n' + '\n'.join(map(str, self.orders))
        #return f'{self.title}\n {self.orders}\n' + '\n'.join(map(str, self.orders))

   # return f'{self.title}\n' + '\n'.join(map(str, self.__students))

goods_1 = Goods(6000, "Phone", 180)
goods_2 = Goods(10000, "Tv", 3)
goods_3 = Goods(2000, "Watch", 50)


buyer_1 = Buyer("Ivanov", "Ivan", "+380 96 918 5 912")
buyer_2 = Buyer("Petrov", "Peter", "+380 97 318 5 320")
buyer_3 = Buyer("Sidorov", "Sergey", "+380 93 518 5 320")


ordering = Order('Order list:')
ordering.add_orders(goods_1)
ordering.add_orders(goods_2)
ordering.add_orders(goods_3)
print(ordering)
total = ordering.sum_orders()
print(total)
print(total)







# А вы сохраните все купленные товары в список.
# А потом если нужно вычислить сумму заказа то просто циклом
# пройдите по всем элементам списка и вычисляйте сумму.

