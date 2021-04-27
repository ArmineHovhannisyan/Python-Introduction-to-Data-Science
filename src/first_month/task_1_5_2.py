class Money:

    def __init__(self, amnt, cur):
        self.__amount = amnt
        self.__currency = cur


    def print(self):
        print(str(self.__amount) + ' ' + self.__currency)

    def sum(self, money):
        if(self.__currency == money.__currency):
           self.__amount += money.__amount
           return  self
        else:
           print('Cant calculate sum of two different currencies. Please implement converter method')

    def sub(self, money):
        if(self.__currency == money.__currency):
            if(self.__amount  >= money.__amount):
                self.__amount -= money.__amount
                return  self
            else:
                print('First amount should be greater or equal to second')
        else:
           print('Cant calculate sub of two different currencies. Please implement converter method')


def main():
    m1 = Money(5, 'usd')
    m1.print()
    m2 = Money(11, 'usd')
    m3 = Money(12, 'eur')
    m2.print()
    m3.print()
    m1.sum(m2)
    m1.print()
    m1.sum(m3)
    m1.print()
    m1.sub(m2)
    m1.print()
    m2.sub(m1)
    m2.print()
    m1.sub(m3)
    m1.print()


main()