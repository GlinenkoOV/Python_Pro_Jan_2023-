class Goods:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        print(f"Product description: {self.price} UAH,{self.description},{self.dimensions} g")


    def __str__(self):
        return f'{self.price} {self.description} {self.dimensions}'

    def get_sum(self):
        for price in self.price():
            return sum(self.price)

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


    def __str__(self):
        return f'{self.title}\n' +'\n'.join(map(str, self.orders))



goods_1 = Goods(6000, "Phone", 180)
goods_2 = Goods(10000, "Tv", 3)
goods_3 = Goods(2000, "Watch", 50)

buyer = Buyer("Ivanov", "Ivan", "+380 96 918 5 912")

ordering = Order('Order list:')
ordering.add_orders(goods_1)
ordering.add_orders(goods_2)
ordering.add_orders(goods_3)
print(ordering)

