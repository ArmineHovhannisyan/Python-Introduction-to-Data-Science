class Money:

    def __init__(self, amnt, cur):
        self.__amount = amnt
        self.__currency = cur


    def Print(self):
        print(str(self.__amount) + ' ' + self.__currency)

    def Sum(self, money):
        if(self.__currency == money.__currency):
           self.__amount += money.__amount
           return  self
        else:
           print('Cant calculate sum of two different currencies. Please implement converter method')

    def Sub(self, money):
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
    m1.Print()
    m2 = Money(11, 'usd')
    m3 = Money(12, 'eur')
    m2.Print()
    m3.Print()
    m1.Sum(m2)
    m1.Print()
    m1.Sum(m3)
    m1.Print()
    m1.Sub(m2)
    m1.Print()
    m2.Sub(m1)
    m2.Print()
    m1.Sub(m3)
    m1.Print()


main()