# by Paulina Czempiel
import operator


class IllegalCarError(Exception):
    # exception raised for errors in the car input
    def __init__(self, message):
        self.message = message


class Car:
    # initializer with instance attributes
    def __init__(self, pax_count, car_mass, gear_count):
        try:
            if 1 < pax_count < 5:
                # number of passengers
                self.pax_count = pax_count
            else:
                raise IllegalCarError('Number of passengers cannot be greater than 5 or less than 1: ' + str(pax_count))
            if car_mass < 2001:
                # mass of the empty car
                self.car_mass = car_mass
            else:
                raise IllegalCarError('Mass of car cannot be greater than 2000 kg: ' + str(car_mass))
        except IllegalCarError as exp:
            print('Invalid input! ' + exp.message)
        # number of gears
        self.gear_count = gear_count
        # the total mass estimate of a car instance (av person is 70 kg)
        self.total_mass = pax_count * 70 + car_mass

    pax_count = property(operator.attrgetter('_pax_count'))

    @pax_count.setter
    def pax_count(self, value):
        try:
            if not 1 < value < 5:
                raise IllegalCarError('Number of passengers cannot be greater than 5 or less than 1: ' + str(value))
            else:
                self._pax_count = value
        except IllegalCarError as exp:
            print('Invalid input! ' + exp.message)

    car_mass = property(operator.attrgetter('_car_mass'))

    @car_mass.setter
    def car_mass(self, value):
        try:
            if not value < 2001:
                raise IllegalCarError('Mass of car cannot be greater than 2000 kg: ' + str(value))
            else:
                self._car_mass = value
        except IllegalCarError as exp:
            print('Invalid input! ' + exp.message)


c = Car(3, 1600, 5)
c.pax_count = 6
c.pax_count = 4
# print(c.pax_count)


wrong_car_1 = Car(3, 2001, 5)
wrong_car_2 = Car(9, 1932, 1)

