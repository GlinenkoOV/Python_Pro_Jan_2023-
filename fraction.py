class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return str(self.a) + "/" + str(self.b)

    def __eq__(self, other):
        return self.a / self.b == other.a / other.b

    def __gt__(self, other):
        return self.a / self.b > other.a / other.b

    def __lt__(self, other):
        return self.a / self.b < other.a / other.b

    def __add__(self, other):

        return Fraction(self.a + other.a, self.b + other.b)


    def __sub__(self, other):

        return Fraction(self.a - other.a, self.b - other.b)

    def __mul__(self, other):

        return Fraction(self.a * other.a, self.b * other.b)


frac_1 = Fraction(2, 4)
print(frac_1)

frac_2 = Fraction(3, 6)
print(frac_2)

print(frac_1 == frac_2)
print(frac_1 > frac_2)
print(frac_1 < frac_2)

print(frac_1 + frac_2)

print(frac_1 - frac_2)

print(frac_1 * frac_2)