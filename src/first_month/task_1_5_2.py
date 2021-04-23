class Money:
    amount = 0
    currency = ''

    def __init__(self, amnt, cur):
        self.amount = amnt
        self.currency = cur


    def Print(self):
        print(str(self.amount) + ' ' + self.currency)

    def Sum(self, money):
        if(self.currency == money.currency):
           sum = self.amount + money.amount
           print('Sum is equal ' + str(sum) + ' ' + self.currency)
        else:
           print('Cant calculate sum of two different currencies. Please implement converter method')

    def Sub(self, money):
        if(self.currency == money.currency):
            if(self.amount  >= money.amount):
                sub = self.amount - money.amount
                print('Sub is equal ' + str(sub) + ' ' + self.currency)
            else:
                print('First amount should be greater or equal to second')
        else:
           print('Cant calculate sub of two different currencies. Please implement converter method')


def main():
    m1 = Money(5, 'usd')
    m1.Print()
    m2 = Money(10, 'usd')
    m3 = Money(10, 'eur')
    m2.Print()
    m3.Print()
    m1.Sum(m2)
    m1.Sum(m3)
    m1.Sub(m2)
    m2.Sub(m1)
    m1.Sub(m3)


main()