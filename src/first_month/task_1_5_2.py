class Money:

    def __init__(self, amnt, cur):
        try:
            if not (isinstance(amnt, int) or isinstance(amnt, float)):
                raise TypeError
        except TypeError:
            print('amount should be number')

        try:
            if not (isinstance(cur, str)):
                raise TypeError
        except TypeError:
            print('currency should be string')

        else:
            try:
                if amnt < 0:
                    raise ValueError
            except ValueError:
                print('amount cant be negative')

            else:
                self.__amount = amnt
                self.__currency = cur

    def __repr__(self):
        return str(self.__amount) + ' ' + self.__currency

    def __add__(self, money):
        if self.__currency == money.__currency:
            self.__amount += money.__amount

        else:
            print('Cant calculate sum of two different currencies. Please implement converter method')

    def __sub__(self, money):
        if self.__currency == money.__currency:
            if self.__amount >= money.__amount:
                self.__amount -= money.__amount

            else:
                print('First amount should be greater or equal to second')
        else:
            print('Cant calculate sub of two different currencies. Please implement converter method')


def main():
    m0 = Money(-10, 'usd')
    m0 = Money('58', 8)
    m1 = Money(5, 'usd')
    print(m1)
    m2 = Money(11, 'usd')
    m3 = Money(12, 'eur')
    print(m2)
    print(m3)
    m1 + m2
    print(m1)
    m1 + m3
    print(m1)
    m1 - m2
    print(m1)
    m2 - m2
    print(m2)
    m1 - m3
    print(m1)

main()


