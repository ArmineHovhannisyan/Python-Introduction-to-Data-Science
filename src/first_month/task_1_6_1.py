class Rational:
    def __init__(self, n, d):
        if d == 0:
            print('denumerator cant be 0')
        _gcd = self.gcd(n, d)
        self.numerator = n // _gcd
        self.denumerator = d // _gcd

    def gcd(self, a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    def lcm(self, a, b):
        return a * b // (self.gcd(a, b))

    def __repr__(self):
        print(str(self.numerator) + '/' + str(self.denumerator))

    def __str__(self):
         if self.numerator == self.denumerator:
             return '1'
         return str(self.numerator) + '/' + str(self.denumerator)

    def __eq__(self, other):
        s = Rational(self.numerator, self.denumerator)
        o = Rational(other.numerator, other.denumerator)
        return s.numerator == o.numerator and s.denumerator == o.denumerator

    def __add__(self, other):
        a = self.lcm(self.denumerator, other.denumerator)
        b = self.numerator * (a // self.denumerator) + other.numerator * (a // other.denumerator)
        return  Rational(b, a)

    def __sub__(self, other):
        a = self.lcm(self.denumerator, other.denumerator)
        b = self.numerator * (a // self.denumerator) - other.numerator * (a // other.denumerator)
        return Rational(b, a)

    def __mul__(self, other):
        a = self.numerator * other.numerator
        b = self.denumerator * other.denumerator
        return Rational(a, b)

    def __floordiv__(self, other):
        a = self.numerator * other.denumerator
        b = self.denumerator * other.numerator
        return Rational(a, b)

    def __gt__(self, other):
        _lcm = self.lcm(self.denumerator, other.denumerator)
        return self.numerator * (_lcm // self.denumerator) > other.numerator * (_lcm // other.denumerator)

    def __ge__(self, other):
        _lcm = self.lcm(self.denumerator, other.denumerator)
        return self.numerator * (_lcm // self.denumerator) >= other.numerator * (_lcm // other.denumerator)

    def __lt__(self, other):
        _lcm = self.lcm(self.denumerator, other.denumerator)
        return self.numerator * (_lcm // self.denumerator) < other.numerator * (_lcm // other.denumerator)

    def __le__(self, other):
        _lcm = self.lcm(self.denumerator, other.denumerator)
        return self.numerator * (_lcm // self.denumerator) <= other.numerator * (_lcm // other.denumerator)

    def __pow__(self, n):
        a = self.numerator ** n
        b = self.denumerator ** n
        return Rational(a, b)







r1 = Rational(15,8)
r2 = Rational(5,4)

r = r1 + r2
print(r)
r = r1 - r2
print(r)
r = r1 * r2
print(r)
r = r1 // r2
print(r)

print(r1 > r2)
print(r1 < r2)
print(r1 >= r2)
print(r1 <= r2)


print(r2 ** 3)

r = Rational(2,0)



















