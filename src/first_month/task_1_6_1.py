class Rational:
    def __init__(self, n, d):
        try:
            if not (isinstance(n, int) or isinstance(d, int)):
                raise TypeError
        except TypeError:
            print('numerator and denumerator should be integer')
        else:
            try:
                if d == 0:
                    raise ZeroDivisionError
            except ZeroDivisionError:
                print('denumerator cant be 0')
            else:
                _gcd = Rational.gcd(n, d)
                self.numerator = n // _gcd
                self.denumerator = d // _gcd  #gcd cant be 0. no need to check ZeroDivisionError

    @staticmethod
    def gcd(a, b):
        while a != b:
            if a > b:
                a = a - b
            else:
                b = b - a
        return a

    @staticmethod
    def lcm(a, b):
        return a * b // (Rational.gcd(a, b))

    def __repr__(self):
        return str(self.numerator) + '/' + str(self.denumerator)

    def __str__(self):
        if self.numerator == self.denumerator:
            return '1'
        return str(self.numerator) + '/' + str(self.denumerator)

    def __eq__(self, other):
        s = Rational(self.numerator, self.denumerator)
        o = Rational(other.numerator, other.denumerator)
        return s.numerator == o.numerator and s.denumerator == o.denumerator

    def __add__(self, other):
        a = Rational.lcm(self.denumerator, other.denumerator)
        try:
            b = self.numerator * (a // self.denumerator) + other.numerator * (a // other.denumerator)
        except ZeroDivisionError:
            print('denumerator cant be 0')
        else:
            return  Rational(b, a)

    def __sub__(self, other):
        a = Rational.lcm(self.denumerator, other.denumerator)
        try:
            b = self.numerator * (a // self.denumerator) - other.numerator * (a // other.denumerator)
        except ZeroDivisionError:
            print('denumerator cant be 0')
        else:
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
        _lcm = Rational.lcm(self.denumerator, other.denumerator)
        return self.numerator * (_lcm // self.denumerator) > other.numerator * (_lcm // other.denumerator)

    def __ge__(self, other):
        _lcm = Rational.lcm(self.denumerator, other.denumerator)
        return self.numerator * (_lcm // self.denumerator) >= other.numerator * (_lcm // other.denumerator)

    def __lt__(self, other):
        _lcm = Rational.lcm(self.denumerator, other.denumerator)
        return self.numerator * (_lcm // self.denumerator) < other.numerator * (_lcm // other.denumerator)

    def __le__(self, other):
        _lcm = Rational.lcm(self.denumerator, other.denumerator)
        return self.numerator * (_lcm // self.denumerator) <= other.numerator * (_lcm // other.denumerator)

    def __pow__(self, n):
        a = self.numerator ** n
        b = self.denumerator ** n
        return Rational(a, b)


r0 = Rational('5', '7')
r1 = Rational(15, 8)
r2 = Rational(5, 4)

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

r = Rational(2, 0)



















