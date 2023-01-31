import math
class Rational:
    def __init__(self, a: int, b: int):
        if not isinstance(a, int):
            raise TypeError('numerator must be int number.')
        if not isinstance(b, int):
            raise TypeError('denumerator must be int number.')
        if b == 0:
            raise ZeroDivisionError()
        self.a = a
        self.b = b
    # def __add__(self, other):
    #     new_a = self.a * other.b + other.a * self.b
    #     new_b = self.b * other.b
    #     return Rational(new_a, new_b)

    def __add__(self, other):
       if isinstance(other, int):
           return Rational(self.a  + other * self.b, self.b )

       if isinstance(other, Rational):
           return Rational(self.a * other.b + other.a * self.b, self.b * other.b)

       return NotImplemented
    def __iadd__(self, other):
        if isinstance(other, int):
            self.a = self.a + other * self.b
            return self
        if isinstance(other, Rational):
            self.a = self.a * other.b + other.a * self.b
            self.b = self.b * other.b
            return self
        return NotImplemented
    def __radd__(self, other):
        if isinstance(other, int):
            self.a = self.a + other * self.b
            return self
        if isinstance(other, Rational):
            self.a = self.a * other.b + other.a * self.b
            self.b = self.b * other.b
            return self
        return NotImplemented
    def __eq__(self, other):
        tmp = math.gcd()
        self.a //= tmp
        self.b //= tmp

        if self.a < 0 and self.b < 0:
            self.a *= -1
            self.b *= -1

        tmp = math.gcd(other.a, other.b)
        other.a //= tmp
        other.b //= tmp

        return (self.a, self.b) == (other.a, other.b)

    def __str__(self):
        tmp = math.gcd(self.a, self.b)
        self.a //= tmp
        self.b //= tmp

        if self.a < self.b:
            return f'{sign}{abs(self.a)} / {abs(self.b)}'
        if self.a == self.b:
            return f'1'
        if self.a > self.b:
            return f'{sign}{abs(self.a) // abs(self.b)} {abs(self.a) % abs(self.b)}/{abs(self.b)}'


    def __str__(self):
        return f'{self.a} / {self.b}'

a = Rational(1, 2)
b = Rational(3, 4)
c = Rational(4, 5)
res = a + b

print(a+ b)
print(a + 2)
a += 1
print(a)
print(1 + a)
x = Rational(-1, -3)
y = Rational(-3, 3)
z = Rational(6, -4)
print(x, y, z, sep='\n')
