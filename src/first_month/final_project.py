# Hotel's rooms reservation system

class Room:

    def __init__(self, _type, count):
        self.__type = _type
        self.__count = count

    def __repr__(self):
        return self.__type + ': available ' + str(self.__count)

    def get_type(self):
        return self.__type

    def get_count(self):
        return self.__count

    def reserve(self, count):
        if self.__count == 0:
            print('There are no free ' + self.__type + ' rooms to reserve')
        else:
            self.__count -= count

    def checkout(self, count):
        self.__count += count

    def set_count(self, count):
        if count > 0:
            self.__count = count


class Hotel:

    def __init__(self, name):

        self.__name = name
        self.__rating = 0
        self.__rater_count = 0
        self.__rooms = [Room('single', 0), Room('double', 0), Room('penthouse', 0)]

    def __repr__(self):
        return self.__name + ': rate ' + str(self.__rating)

    def get_rate(self):
        return self.__rating

    def reserve(self, _type, _count):
        for r in self.__rooms:
            if r.get_type() == _type:
                r.reserve(_count)

    def checkout(self, _type, _count):
        for r in self.__rooms:
            if r.get_type() == _type:
                r.checkout(_count)

    def rate(self, rating):
        try:
            if rating < 0 or rating > 10:
                raise ValueError
        except ValueError:
            print('Rate should be between 0 and 10')
        else:
            self.__rater_count += 1
            self.__rating = round(((self.__rater_count - 1) * self.__rating + rating) / self.__rater_count, 1)

    def get_rooms(self):

        return self.__rooms

    def add_room(self, _type, _count):
        _rooms = []
        r_added = Room(_type, _count)

        for r in self.__rooms:
            if _type == r.get_type():
                r.set_count(r.get_count() + _count)

    def remove_room(self, _type, _count):
        for r in self.__rooms:
            if r.get_type() == _type:
                r.set_count(r.get_count() - _count)

                try:
                    if r.get_count() - _count < 0:
                        raise ValueError
                except ValueError:
                    print('There are no available ' + str(_count) + ' ' + _type + ' rooms to remove')


hotel = Hotel('Hotel')
print(hotel)

hotel.rate(5)

hotel.rate(5)
hotel.rate(4)
hotel.rate(4)
hotel.rate(15)
print(hotel)


hotel.add_room('single', 3)
print(hotel.get_rooms())
hotel.reserve('single', 2)
print(hotel.get_rooms())
hotel.checkout('single', 2)
print(hotel.get_rooms())


hotel.add_room('single', 2)
hotel.add_room('double', 2)

print(hotel.get_rooms())

hotel.add_room('penthouse', 2)
hotel.add_room('penthouse', 2)
hotel.add_room('double', 2)
print(hotel.get_rooms())

hotel.remove_room('double', 7)



