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
        self.__count = count


class Hotel:

    def __init__(self, name, rating, rater_count, _rooms):
        try:
            if rating < 0 or rating > 10:
                raise ValueError
        except ValueError:
            print('Rate should be between 0 and 10')

        else:
            self.__name = name
            self.__rating = rating
            self.__rater_count = rater_count
            self.__rooms = _rooms

    def __repr__(self):
        return self.__name + ': rate ' + str(self.__rating)

    def get_rate(self):
        return self.__rating

    def reserve(self, room):
        for r in self.__rooms:
            if r.get_type() == room.get_type():
                r.reserve(room.get_count())

    def checkout(self, room):
        for r in self.__rooms:
            if r.get_type() == room.get_type():
                r.checkout(room.get_count())

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
        available_rooms = ''
        for r in self.__rooms:
            available_rooms += r.get_type() + ' ' + str(r.get_count()) + ' '
        return available_rooms

    def add_room(self, _rooms):
        added_rooms = []
        #existing_types = []

        for r_current in self.__rooms:
            for r_added in _rooms:
                if r_current.get_type() != r_added.get_type():
                    added_rooms.append(r_added)
                else:
                    r_current.set_count(r_current.get_count() + r_added.get_count())

        self.__rooms.extend(added_rooms)

    def remove_room(self, _rooms):
        for r_current in self.__rooms:
            for r_removed in _rooms:
                if r_current.get_type() == r_removed.get_type():
                    r_current.set_count(r_current.get_count() - r_removed.get_count())

                else:
                    print('There are no ' + r_removed.get_type() + ' rooms to remove')


r1 = Room('single', 4)
print(r1)

room_for_reserve = Room('single', 2)
rooms = [r1]

hotel1 = Hotel('Hotel', 100, 100, rooms)
hotel = Hotel('Hotel', 0, 0, rooms)
print(hotel)

hotel.rate(5)

hotel.rate(5)
hotel.rate(4)
hotel.rate(4)
hotel.rate(15)
print(hotel)


print(hotel.get_rooms())
hotel.reserve(room_for_reserve)
print(hotel.get_rooms())
hotel.checkout(room_for_reserve)
print(hotel.get_rooms())


added_room1 = Room('single', 3)
added_room2 = Room('single', 2)
added_room3 = Room('double', 2)
rooms_added = [added_room1, added_room2, added_room3]

added_room4 = Room('double', 2)


hotel.add_room(rooms_added)
rooms_added2 = [added_room4]
print(hotel.get_rooms())

hotel.add_room(rooms_added2)
print(hotel.get_rooms())

#hotel.add_room([])


